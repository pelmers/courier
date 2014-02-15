plugins/
--------

Python sub-modules here will be automatically added as plugins to pythrust.
Each plugin is expected to have:
 - `PLUGIN_NAME`, str name for the plugin
 - `process(path, args)`, function that process path with args
 - docstring describing usage
