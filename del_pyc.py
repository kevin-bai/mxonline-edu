import os
path = 'F:\webProject\mxonline'
for prefix, dirs, files in os.walk(path):
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            print 'del:' + filename
            os.remove(filename)