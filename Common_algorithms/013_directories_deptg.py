"""
    List directories with a specified depth in Python

    import os,string
    path = '.'
    path = os.path.normpath(path)
    res = []
    for root,dirs,files in os.walk(path, topdown=True):
        depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
        if depth == 2:
            # We're currently two directories in, so all subdirs have depth 3
            res += [os.path.join(root, d) for d in dirs]
            dirs[:] = [] # Don't recurse any deeper
    print(res)

"""

import os,string
path = '/data/'
path = os.path.normpath(path)
res = []
for root,dirs,files in os.walk(path, topdown=True):
    depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
    if depth == 3:
        # We're currently two directories in, so all subdirs have depth 3
        res += [os.path.join(root, d) for d in dirs]
        dirs[:] = [] # Don't recurse any deeper
print(res)