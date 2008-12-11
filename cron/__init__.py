#!/usr/bin/env python
"""
This is the template for all cron scripts.
"""

def run():
    pass

if __name__ == '__main__':
    from pbs.utils.django_tools.deployment import bootstrap_script
    bootstrap_script(__file__, ['src', 'notabs'])
    run()
