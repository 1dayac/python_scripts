__author__ = 'dima'
from Bio import SearchIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import sys
#1 parameter - dom-table
#2 parametr - reading frame [1,2,3,-1,-2,-3]
#3 - fasta file with reference genome
#4 - out_dir

input_handle = open(sys.argv[3], "rU")
record_dict = SeqIO.to_dict(SeqIO.parse(input_handle, "fasta"))
output_handle = open(sys.argv[4] + "a_domains.fasta", "a")
output_handle2 = open(sys.argv[4] + "restricted_edges.fasta", "a")

hmmer_result = SearchIO.read(sys.argv[1], 'hmmsearch3-domtab')
curr=1
used = set()
for hit in hmmer_result:
    for hsp in hit:
        hit_start = hsp.hit_range[0]
        hit_end = hsp.hit_range[1]
        domain_start = hsp.query_range[0]
        domain_end = hsp.query_range[1]
        if domain_end - domain_start > 200:
            if hit.id[:-2] not in used:
                SeqIO.write(record_dict[hit.id[:-2]], output_handle2, "fasta")
            used.add(hit.id[:-2])
            if int(sys.argv[2]) > 0:

                record = SeqRecord(record_dict[hit.id[:-2]][(hsp.env_start)*3 + int(sys.argv[2]) - 1 : (hsp.env_end - 1)*3 + int(sys.argv[2]) - 1].seq, id=str((hsp.env_start)*3 + int(sys.argv[2]) - 1)+"_"+str((hsp.env_end - 1)*3 + int(sys.argv[2]) - 1), description="")
                SeqIO.write(record, output_handle, "fasta")
            if int(sys.argv[2]) < 0:
                rcRecord = record_dict[hit.id[:-2]].seq.reverse_complement()
                record = SeqRecord(rcRecord[(hsp.env_start)*3 + abs(int(sys.argv[2])) - 1 : (hsp.env_end - 1)*3 + abs(int(sys.argv[2])) - 1], id=str(len(rcRecord) - ((hsp.env_end)*3 - abs(int(sys.argv[2]))))+"_"+str(len(rcRecord) - ((hsp.env_start)*3 - abs(int(sys.argv[2]))-1))+"_rc" , description="")
                SeqIO.write(record, output_handle, "fasta")


            curr += 1
output_handle.close()