from Bio import SeqIO, SeqRecord
from Bio import Alphabet
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
import Bio
import itertools
import sys
import random
from random import shuffle



file_l = str(sys.argv[1])
file_out_l = str(sys.argv[2]) + "/input.fasta"
format = "fasta"
records_f = SeqIO.parse(open(file_l,"rU"), format)

mismatch_rate = 0.02
insert_rate = 0.005
del_rate = 0.0025

alphabet = ["A","C","G","U"]
def get_new_read(old_read):
    seq = old_read.seq
    newseq = Bio.Seq.Seq('')
    for i in range(0, len(seq)):
        rand = random.uniform(0,1)
        if rand > mismatch_rate:
            newseq = newseq + seq[i]
            continue
        if rand <= mismatch_rate and rand > insert_rate:
            new_nucl = alphabet[random.randint(0,3)]
            while seq[i] ==  new_nucl:
                new_nucl = alphabet[random.randint(0,3)]
            newseq = newseq + new_nucl
            continue
        if rand <= insert_rate and rand > del_rate:
            continue
        if rand < del_rate:
            new_nucl = alphabet[random.randint(0,3)]
            newseq = newseq + new_nucl

            continue
    return newseq



records = [r for r in records_f]
new_records = []
for i in range(0,50):
    number_of_read = random.randint(0,len(records) - 1)
    read = records[number_of_read]
    new_read = get_new_read(read)
    record = SeqRecord.SeqRecord(new_read, id = str(random.randint(0,100000)))
    new_records.append(record)

for i in range(0,10):
    species = random.sample(range(0, len(records)), 2)
    read1 = records[species[0]]
    read2 = records[species[1]]
    new_read1 = get_new_read(read1)
    new_read2 = get_new_read(read2)
    breakpoint1 = random.randint(100, len(new_read1)/2)
    breakpoint2 = random.randint(breakpoint1, len(new_read2) - 100)
    start = new_read[:breakpoint1]
    end = new_read2[breakpoint2:]
    res = start+end
    #print(start)
    #print(end)
    tada = random.randint(0,100000)
    print(tada)
    record = SeqRecord.SeqRecord(res, id = str(tada))
    new_records.append(record)
shuffle(new_records)

count = SeqIO.write(new_records, file_out_l, "fasta")