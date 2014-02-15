"""
autocomplete plugin
Autocompletes paths by matching a list of possibilities
given by some environment variable.
Usage:
    autocomplete path ENV_VAR [-d DEPTH]
Returns a list of the possible autocompletions of path by using ENV_VAR
as a list of possible matches and including subdirectories up
to depth DEPTH (default: 2).
"""

PLUGIN_NAME = 'autocomplete'

import os, sys
import os.path

def process(path, args):
    if not args:
        print('Expected environment variable name in args list')
        return []
    # default depth is 2 unless -d is given for depth
    depth = 2 if '-d' not in args else int(args[args.index('-d')+1])
    env = os.getenv(args[0])
    # set env to empty str instead of None if not found
    env = '' if not env else env
    paths = [p for p in env.split(':') if os.path.isdir(p)]
    if len(paths) == 0:
        print('autocomplete could not find valid paths from given env.')
        return []
    # lowercase everything, we want case insensitive matches
    # we're also only matching on the last part of each path
    path_match = path.lower()
    possible_matches = [os.path.split(p)[1].lower() for p in paths]
    # next we walk depth down each path in env and add to possible matches
    prev_layer = [p for p in paths if os.path.isdir(p)]
    for _ in range(depth):
        layer = [os.path.join(p, f) for p in prev_layer
                for f in os.listdir(p) if os.path.isdir(os.path.join(p,f))]
        possible_matches.extend([os.path.split(p)[1].lower() for p in layer])
        paths.extend([p for p in layer])
        prev_layer = layer
    # now we get the indices of the matches and map them back to paths
    matches = [paths[m] for m in [idx for (idx, match) in
        enumerate(possible_matches) if match.find(path_match) != -1]]
    return matches
