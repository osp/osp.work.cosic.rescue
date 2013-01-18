import os
import sys
import site 


alldirs = ['/home/stdin/www/cosic.stdin.fr/venv/lib/python2.6/site-packages/']


# remember original sys.path.
prev_sys_path = list(sys.path) 

# add each new site-packages directory.
for directory in alldirs:
  site.addsitedir(directory)

# reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path 

sys.path.append('/home/stdin/www/cosic.stdin.fr/cosic/')
sys.path.append('/home/stdin/www/cosic.stdin.fr/')

import cosic
import bottle

os.chdir(os.path.dirname(__file__))

application = bottle.default_app()
