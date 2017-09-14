__author__ = 'dima'

import sys
import os
import glob

path_to_antismash_folder = sys.argv[1]
path_to_txt_reports_folder = path_to_antismash_folder + os.sep + "txt/"

list_of_files = glob.glob(path_to_txt_reports_folder + "*BGC.txt")
print(list_of_files)
result = []

for file in list_of_files:
    with open(file, 'r') as infile:
        lines = infile.readlines()
        for x in range(1, len(lines)):
            result.append(lines[x].split('\t'))
answer_file = path_to_antismash_folder + os.sep + "summary.txt"
with open(answer_file, 'w') as outfile:
    for line in result:
        outfile.write('\t'.join([line[0], line[1], line[3].split(';')[0], line[3].split(';')[1]]))
        outfile.write('\n')