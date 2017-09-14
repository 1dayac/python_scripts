__author__ = 'dima'
import os
import sys
from Bio import SeqIO

pathsep = "/"
directory = sys.argv[1] + pathsep + "fasta" + pathsep
outputfile = sys.argv[1] + pathsep + "report.txt"

f = open(outputfile, 'w')


def FindPercentId(filename):
    handle = open(filename, "rU")
    line = handle.readline()
    line = handle.readline()
    line = handle.readline()
    print("Here")
    print(float(line.split()[9]))
    print("Here")

    return float(line.split('|')[3])


def FindNumOfMIss(filename):
    handle = open(filename, "rU")
    for line in handle:
        if line.startswith("# misassemblies"):
            return int(line.split()[2])



def AnalyzeAssembly(assembly_file, reference_file, dataset_name, prefix):
    reference_handle = open(reference_file, "rU")
    handle = open(assembly_file, "rU")

    reference_len = len(list(SeqIO.parse(reference_handle, "fasta"))[0].seq)
    idx = 0
    for record in SeqIO.parse(handle, "fasta"):
        idx += 1
        if len(record.seq) > reference_len * 0.9:
            output_handle = open(sys.argv[1] + pathsep +  "temp.fasta", 'w')
            SeqIO.write(record, output_handle, "fasta")
            output_handle.close()
            os.system("quast.py -R " + reference_file + " " + sys.argv[1] + pathsep +  "temp.fasta -o " + sys.argv[1] + pathsep + "quast_reports_" + prefix + pathsep + dataset_name)
            if FindNumOfMIss(sys.argv[1] + pathsep + "quast_reports_" + prefix + pathsep + dataset_name + pathsep + "report.tsv") == 0 and FindPercentId(sys.argv[1] + pathsep + "quast_reports_" + prefix + pathsep + dataset_name + pathsep + "contigs_reports/nucmer_output/" + "temp.coords") > 90.0 :
                f.write("+")
                f.write('\t')
                handle.close()
                reference_handle.close()

                return
        if idx > 20:
            break
    f.write("-")
    f.write('\t')

    handle.close()
    reference_handle.close()

def ProcessDataset(dataset_name):
    antispades_assembly = sys.argv[1] + pathsep + "antispades_assembly" + pathsep + dataset_name + pathsep + "scaffolds.fasta"
    antispades_orderings = sys.argv[1] + pathsep + "antispades_assembly" + pathsep + dataset_name + pathsep + "K55" + pathsep + "orderings.fasta"
    spades_assembly = sys.argv[1] + pathsep + "spades_assembly" + pathsep + dataset_name + pathsep + "scaffolds.fasta"
    reference_path = sys.argv[1] + pathsep + "fasta" + pathsep + dataset_name + ".fasta"

    f.write(dataset_name)
    f.write('\t')

    AnalyzeAssembly(spades_assembly, reference_path, dataset_name, "spades")
    AnalyzeAssembly(antispades_assembly, reference_path, dataset_name, "antispades")
    AnalyzeAssembly(antispades_orderings, reference_path, dataset_name, "antispades")
    f.write('\n')
    f.flush()
    return

f.write("\t SPAdes Assembly \t antiSPAdes assembly \n")
for filename in os.listdir(directory):
    if filename.endswith(".fasta"):
        dataset_name = os.path.splitext(filename)[0]
        ProcessDataset(dataset_name)

f.close()