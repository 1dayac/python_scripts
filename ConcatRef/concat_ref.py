__author__ = 'dima'

from Bio import SeqIO
from Bio import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqRecord
import sys

#Usage: python concat_ref.py input_file.fasta output_file.fasta
#Make reference 10X-compatible
input_file = sys.argv[1]
output_file = sys.argv[2]

insert_seq = "N" * 500
seq = Seq.Seq("", generic_dna)
for record in SeqIO.parse(input_file, "fasta"):
    seq += record.seq
    seq += insert_seq

new_record = SeqRecord.SeqRecord(seq, id = "concatenated_reference")
with open(output_file, "w") as output_handle:
    SeqIO.write(new_record, output_handle, "fasta")

