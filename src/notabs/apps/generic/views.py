from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sites.models import Site, RequestSite
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache

from pbs.django.utils.http import get_redirect_url

def index(request):
    return render_to_response('index.html', {
        }, context_instance=RequestContext(request))

@never_cache
def login(request, template_name='login.html', redirect_field_name=REDIRECT_FIELD_NAME, url_name=None):
    "Displays the login form and handles the login action."
    redirect_to = get_redirect_url(request, default_url=reverse(url_name or 'index'))
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            from django.contrib.auth import login
            login(request, form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        form = AuthenticationForm(request)
    request.session.set_test_cookie()
    if Site._meta.installed:
        current_site = Site.objects.get_current()
    else:
        current_site = RequestSite(request)
    return render_to_response(template_name, {
        'form': form,
        redirect_field_name: redirect_to,
        'site_name': current_site.name,
    }, context_instance=RequestContext(request))

@never_cache
def logout(request, url_name=None):
    from django.contrib.auth import logout
    logout(request)
    redirect_to = get_redirect_url(request, default_url=reverse(url_name or 'index'))
    return HttpResponseRedirect(redirect_to)

@never_cache
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from django.contrib.auth import authenticate, login
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
        
    return render_to_response('register.html', {
        'form': form,
        }, context_instance=RequestContext(request))
        
