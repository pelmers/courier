"""
rice plugin

Use rsync via ssh to synchronize local files with Rice's CLEAR network,
autocompletes based on paths defined in environment variable RICE_PATH
Usage:
    rice source_path netID dest_path [rsync_opts]
dest_path is relative to user's home directory on CLEAR, usually
/storage-home/{a-z}/netID/
See 'help rsync' for more information on rsync_opts.

Special usage:
    rice ssh netID
SSH into your CLEAR account
"""

PLUGIN_NAME = 'rice'

import subprocess
import plugins.rsync

def process(path, args):
    env = "RICE_PATH"
    if len(args) < 2:
        # special case: we want to ssh instead
        if path == 'ssh':
            subprocess.call(['ssh', '{}@ssh.clear.rice.edu'.format(args[0])])
            return
        return 'rice plugin expects at least two arguments after source path'
    dest = args[0]
    netid = args[1]
    rsync_opts = args[2:]
    dest = "{0}@ssh.clear.rice.edu:/storage-home/{1}/{0}/{2}".format(
            netid, netid[0], dest)
    return plugins.rsync.process(path, [env, dest]+rsync_opts)
