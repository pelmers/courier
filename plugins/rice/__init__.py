"""
rice plugin

Use rsync via ssh to synchronize local files with Rice's CLEAR network,
autocompletes based on paths defined in environment variable RICE_PATH
Usage:
    rice source_path dest_path netID [rsync_opts]
dest_path is relative to user's home directory on CLEAR, usually
/storage-home/{a-z}/netID/
See 'help rsync' for more information on rsync_opts.
"""

PLUGIN_NAME = 'rice'

import plugins.rsync

def process(path, args):
    env = "RICE_PATH"
    if len(args) < 2:
        return 'rice plugin expects at least two arguments after source path'
    dest = args[0]
    netid = args[1]
    rsync_opts = args[2:]
    dest = "{0}@ssh.clear.rice.edu:/storage-home/{1}/{0}/{2}".format(
            netid, netid[0], dest)
    plugins.rsync.process(path, [env, dest]+rsync_opts)
