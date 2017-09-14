__author__ = 'dima'
from Bio import SeqIO
import sys
import os
from Bio import SeqRecord, Seq

dir = str(sys.argv[1])
out_dir = str(sys.argv[2])

for filename in os.listdir(dir):
    if filename.endswith("fasta"):
        with open(dir + "/" + filename, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                print(record)
                new_record = SeqRecord.SeqRecord(record.seq, id = record.id, description="")
                print(new_record)
                SeqIO.write(new_record, out_dir + "/" + filename, "fasta")