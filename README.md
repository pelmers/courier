courier: process selected directories intelligently and magically.
=========

Brief overview:
---------------
Almost all of courier's functionality is embedded in its powerful and easy to write plugins.
Although not enforced, plugins primarily focus on performing operations on file and folder paths.
See [plugins/help](https://github.com/pelmers/courier/blob/master/plugins/help) for an example of how easy it is to set up plugins.

Basic usage:
------------

 - `help`: shows usage information of other plugins, not much to see here.
 - `autocomplete`: finds matches for a path stem by looking for possibilities defined in some environment variable: `TEST_PATH="/usr/" courier.py autocomplete bin TEST_PATH`
 - `rsync`: builds upon `autocomplete` with rsync: `TEST_PATH="/usr/" courier.py rsync bin TEST_PATH /somewhere/else`
