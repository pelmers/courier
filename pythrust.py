#!/usr/bin/env python3

import sys
if sys.version[0] != '3':
    print("Beware: python version < 3, some features may not behave properly.")

def output_and_exit(msg):
    sys.stderr.write(msg)
    sys.exit(1)

try:
    import plugins
except ImportError:
    output_and_exit('Cannot find any plugins\n')

USAGE = """\
        Usage: {0} plugin path [args]
        Calls on plugin to process path with optional [args].
        Type '{0} help plugin' for more info.
        Available plugins: {1}\
        """.format(sys.argv[0], ' '.join(plugins.plugin_names()))

def main():
    if '-h' in sys.argv:
        print(USAGE)
        return
    try:
        plugin = sys.argv[1]
        path = sys.argv[2]
        args = sys.argv[3:]
    except IndexError:
        output_and_exit('Insufficient arguments supplied.\n{}\n'.format(USAGE))
    if plugin not in plugins.plugin_names():
        output_and_exit('{} not an available plugin.\n{}\n'.format(plugin, USAGE))
    ret = plugins.process(plugin, path, args)
    if ret:
        print(ret)

if __name__ == '__main__':
    main()
