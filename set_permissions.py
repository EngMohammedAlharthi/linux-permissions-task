import os
import stat

filename = 'my_script.py'

with open(filename, 'w') as f:
    f.write('print("Hello World")\n')

mode = stat.S_IRWXU | stat.S_IRWXG | stat.S_IRGRP | stat.S_IXOTH
os.chmod(filename, mode)

print(oct(os.stat(filename).st_mode & 0o777))
