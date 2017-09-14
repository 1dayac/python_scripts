__author__ = 'dima'

import json
import sys
import os
from Bio import SeqIO
pathsep = "/"
root_folder = sys.argv[1]
json_folder = root_folder + pathsep + "json"
genbank_folder = root_folder + pathsep + "genbank"
fasta_folder = root_folder + pathsep + "fasta"

def process_genbank(filename):
    base = os.path.basename(filename)
    name = os.path.splitext(base)[0]

    input_handle = open(filename, "rU")
    outfilename = fasta_folder + pathsep + name + ".fasta"

    output_handle = open(outfilename, "w")
    records = SeqIO.parse(input_handle, "genbank")
    SeqIO.write(records, output_handle, "fasta")
    input_handle.close()
    output_handle.close()

def Check(classes):
    return "NRP" in classes or "Polyketide" in classes

def process_json_file(data):
    classes = data["general_params"]["biosyn_class"]
    return Check(classes)

onlyfiles = [os.path.join(json_folder, f) for f in os.listdir(json_folder) if os.path.isfile(os.path.join(json_folder, f))]
for fn in onlyfiles:
    base = os.path.basename(fn)
    filename = os.path.splitext(base)[0]
    with open(fn) as json_file:
        data = json.load(json_file)
        is_pure_nrp = process_json_file(data)
        if is_pure_nrp:
            if os.path.exists(genbank_folder + pathsep + filename + ".gbk"):
                process_genbank(genbank_folder + pathsep + filename + ".gbk")