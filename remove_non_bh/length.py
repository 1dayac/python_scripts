__author__ = 'dima'

from Bio import SeqIO
import sys


fasta = str(sys.argv[1])
records = SeqIO.parse(open(fasta,"rU"), "fasta")
records_sorted = sorted(records, key = len)
records_sorted = records_sorted[-100:-1]
lens = [len(x.seq) for x in reversed(records_sorted)]
print(lens)

handle = open("coel_top100.fasta", "w")
count = SeqIO.write(records_sorted, handle, "fasta")
handle.close()
