__author__ = 'dima'
import os
from fnmatch import fnmatch
from subprocess import call

root = '/Finn/meleshko/data/HMP.DATASETS/'
pattern1 = "*1.fastq"
pattern2 = "*2.fastq"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern1):
            print(os.path.join(path, name))
            call(["mv", os.path.join(path, name), os.path.join(path,"R1.fastq")])
        if fnmatch(name, pattern2):
            print(os.path.join(path, name))
            call(["mv", os.path.join(path, name), os.path.join(path,"R2.fastq")])
