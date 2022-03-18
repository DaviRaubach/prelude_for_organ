import shutil
import os
import fnmatch

for path, dirs, files in os.walk('./segments'):
    if dirs is not 'backup':
        for f in fnmatch.filter(files,'*.ly'):
            fullname = os.path.abspath(os.path.join(path,f))
            print(fullname)

# shutil.copyfile(original, target)