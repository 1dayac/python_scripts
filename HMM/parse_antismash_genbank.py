__author__ = 'dima'
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import DNAAlphabet
import sys

input_handle = open(sys.argv[1], "rU")
output_handle = open("result_2.fasta", "w")

for hit in SeqIO.parse(input_handle, "genbank"):
        for record in hit.features:
            if record.type == "cluster":
                a = str(record.qualifiers['note'][1])
                if "type: nrps" in a or "type: other:" in a :
                    print(type(record.location))
                    print(record.location)
                    print(a)
                    print(hit.description)
                    print(hit.seq)
                    record = SeqRecord(hit.seq, id = str(hit.description), description=str(record.location.start) + " " + str(record.location.end) + " " + "+" if record.location.strand == 1 else "-")
                    SeqIO.write(record, output_handle, "fasta")
                    print(record)


input_handle.close()
output_handle.close()