__author__ = 'dima'
from Bio import SeqIO
import sys
import os
from Bio import SeqRecord, Seq
from os import listdir, path, system

differ_file = "diffs.txt"
out_file = "res.txt"
max_diff = 10000
handle_diff = open(differ_file, 'w')
handle_res = open(out_file, 'w')
dir = str(sys.argv[1])

for filename in os.listdir(dir):
    coords = []
    if filename.endswith("fasta"):
        system("./extract_A_domain_coords_npspades.sh " + dir + "/" + filename + " temp/")
        for domain_file in os.listdir("/home/dmeleshko/dereplicator/npSPAdes_scripts/temp/"):
            print(domain_file)
            if domain_file.endswith("domains.fasta"):

                for record in SeqIO.parse("temp" + "/" + domain_file, "fasta"):
                    name = record.id.split('_')
                    p = (int(name[0]),int(name[1]))
                    coords.append(p)
        coords.sort()
        print(coords)
        big_gap = False
        for i in range(len(coords) - 1):
            diff = coords[i+1][0] - coords[i][1]
            handle_diff.write(str(diff) + "\n")
            if diff > max_diff:
                big_gap = True
        if big_gap:
            handle_res.write("-")
        else:
            handle_res.write("+")
handle_diff.close()
handle_res.close()