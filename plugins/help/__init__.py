"""
help plugin
Provides help on plugins.
Usage:
    help plugin
"""

import plugins

PLUGIN_NAME = 'help'

def process(plugin, args, _e):
    if plugin not in plugins.plugin_names():
        return "{} plugin not found.".format(plugin)
    else:
        return plugins.available_plugins[plugin].__doc__
