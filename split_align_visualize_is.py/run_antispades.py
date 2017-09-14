__author__ = 'dima'
import os
from fnmatch import fnmatch
from subprocess import call

root = '/Finn/meleshko/data/HMP.DATASETS/'
pattern1 = "*1.fastq"
pattern2 = "*2.fastq"

all_dirs = [x[0] for x in os.walk(root)]
for d in all_dirs:
    if os.path.basename(d).startswith("SRS"):
        dataset_name = os.path.basename(d)
        source_name = os.path.basename(os.path.dirname(d))
#        call(["mkdir", "-p", os.path.join("/Finn/meleshko/meta/antispades_paper/hmp", source_name, dataset_name)])
        call(["/home/dmeleshko/algorithmic-biology/assembler/spades.py", "--anti", "--pe1-1", os.path.join(root, source_name, dataset_name, "R1.fastq"), "--pe1-2", os.path.join(root, source_name, dataset_name, "R2.fastq"), "-o", os.path.join("/Finn/meleshko/meta/antispades_paper/hmp/", source_name, dataset_name)], shell=False)