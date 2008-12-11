import os
SERVER_IDENTIFIER = os.getenv("SERVER_IDENTIFIER")

# import defaults
from notabs.config.base import *

# import overrides
overrides = __import__(
    "notabs.config." + SERVER_IDENTIFIER,
    globals(),
    locals(),
    ["notabs.config"]
)

# apply imported overrides
for attr in dir(overrides):
    # we only want to import settings (which have to be variables in ALLCAPS)
    if attr.isupper():
        # update our scope with the imported variables. We use globals() instead of locals()
        # because locals() is readonly and it returns a copy of itself upon assignment.
        globals()[attr] = getattr(overrides, attr)
