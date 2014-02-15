import os, sys
import os.path
from importlib import import_module

# get a listing of the files in the current directory
plugin_dir = os.path.split(os.path.abspath(__file__))[0]
ls = [os.path.join(plugin_dir, f) for f in os.listdir(plugin_dir)
        if not f.startswith('_')] # exclude underscored names
# go through all the subfolders not starting in underscore
available_plugins = {}
for mod in ['.'.join([os.path.split(plugin_dir)[1], os.path.split(f)[1]])
        for f in ls if os.path.isdir(f)]:
    try:
        available_plugins[mod[mod.rfind('.')+1:]] = import_module(mod)
    except ImportError:
        sys.stderr.write("Error importing plugin {}.\n".format(mod))
        sys.exit(1)

def plugin_names():
    return [getattr(plugin, 'PLUGIN_NAME') for plugin in available_plugins.values()]

def process(plugin, path, args):
    try:
        return available_plugins[plugin].process(path, args)
    except KeyError:
        sys.stderr.write("Error calling {} plugin.\n".format(plugin))
