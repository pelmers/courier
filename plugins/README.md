plugins/
--------

Python sub-modules here will be automatically added as plugins to courier.
Each plugin is expected to have:
 - `PLUGIN_NAME`, str name for the plugin
 - `process(path, args, env)`, function that process path with args and environment variables env
 - docstring describing usage
