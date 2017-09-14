__author__ = 'dima'
from Bio import SeqIO
import itertools
import sys


def interleave(iter1, iter2) :
    for (forward, reverse) in itertools.izip(iter1,iter2):
        if "BH:failed" in forward.id or "BH:failed" in reverse.id:
            continue
        yield forward
        yield reverse

file_l = str(sys.argv[1])
file_r = str(sys.argv[2])

file_out_l = str(sys.argv[3]) + "/filter.fastq"

format = "fastq"

records_f = SeqIO.parse(open(file_l,"rU"), format)
records_r = SeqIO.parse(open(file_r,"rU"), format)

handle = open(file_out_l, "w")
count = SeqIO.write(interleave(records_f, records_r), handle, format)
handle.close()
