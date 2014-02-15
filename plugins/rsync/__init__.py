"""
rsync plugin
Use autocomplete and rsync to update remote files.

Usage:
    rsync source_path ENV_VAR dest_path [rsync_opts]
Call upon rsync to synchronize source_path with dest_path,
where source path is autocompleted based on paths defined in ENV_VAR.
See man rsync for information on rsync_opts.
Default opts: -avz --exclude='*.git'
"""

PLUGIN_NAME = 'rsync'

import subprocess, plugins.autocomplete

def process(path, args):
    if len(args) < 2:
        return 'Rsync plugin expected at least two arguments after path'
    rsync_opts = args[2:]
    env = args[0]
    dest = args[1]
    if not rsync_opts:
        rsync_opts = ['-avz', "--exclude='*.git'"]
    # autocomplete path to get source paths
    source_paths = plugins.autocomplete.process(path, [env])
    for src in source_paths:
        subprocess.call(['rsync']+rsync_opts+[src, dest])
