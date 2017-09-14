__author__ = 'dima'
from Bio import SearchIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import sys
#1 parameter - dom-table
#2 parametr - reading frame [1,2,3,-1,-2,-3]
#3 - fasta file with reference genome
#4 - coordinates of NRPS BGCs

#def ParseDescription()

def Inside(nrps_ranges, a_domain_start, a_domain_end) :
    for range in nrps_ranges:
        if a_domain_start >= range[0] and a_domain_end <= range[1]:
            return True
    return False

nrps_ranges = [(493989, 544920),(3523335, 3603988),(7088264, 7136089)]

fasta_sequence = SeqIO.parse(open(sys.argv[3]),'fasta')
output_handle = open("result.fasta", "a")
ref = next(fasta_sequence).seq
rc_ref = ref.reverse_complement()

hmmer_result = SearchIO.read(sys.argv[1], 'hmmsearch3-domtab')
for hit in hmmer_result:
    print(hit.id)
    for hit2 in hit:
        if hit2.query_end - hit2.query_start > 400:
            if int(sys.argv[2]) > 0:
                if not Inside(nrps_ranges, (hit2.env_start - 1)*3 + int(sys.argv[2]) - 1, (hit2.env_end - 1)*3 + int(sys.argv[2]) - 1):
                    continue
                record = SeqRecord(ref[(hit2.env_start - 1)*3 + int(sys.argv[2]) - 1 : (hit2.env_end - 1)*3 + int(sys.argv[2]) - 1], id=str((hit2.env_start - 1)*3 + int(sys.argv[2]) - 1)+"_"+str((hit2.env_end - 1)*3 + int(sys.argv[2]) - 1), description="")
                SeqIO.write(record, output_handle, "fasta")
            if int(sys.argv[2]) < 0:
                if not Inside(nrps_ranges, len(ref) - ((hit2.env_end - 1)*3 + abs(int(sys.argv[2])) - 1), len(ref) - ((hit2.env_start - 1)*3 + abs(int(sys.argv[2])) - 1)):
                    continue
                #print((hit2.env_start - 1)*3 + abs(int(sys.argv[2])) - 1)
                #print((hit2.env_end - 1)*3 + abs(int(sys.argv[2])) - 1)
                record = SeqRecord(rc_ref[(hit2.env_start - 1)*3 + abs(int(sys.argv[2])) :(hit2.env_end - 1)*3 + abs(int(sys.argv[2]))], id=str(len(ref) - ((hit2.env_end - 1)*3 + abs(int(sys.argv[2])) - 1))+"_"+str(len(ref) - ((hit2.env_start - 1)*3 + abs(int(sys.argv[2])) - 1))+"_rc" , description="")
                SeqIO.write(record, output_handle, "fasta")

output_handle.close()