__author__ = 'dima'
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from subprocess import call
import distutils.dir_util
import sys
#1 - reference
#2 - left reads
#3 - right reads
#4 - output dir

reference_file = str(sys.argv[1])
left_reads_file = str(sys.argv[2])
right_reads_file = str(sys.argv[3])
output_dir = str(sys.argv[4])

distutils.dir_util.mkpath(output_dir)
distutils.dir_util.mkpath(output_dir + os.path.sep + "split_ref")
distutils.dir_util.mkpath(output_dir + os.path.sep + "sam_files")
distutils.dir_util.mkpath(output_dir + os.path.sep + "is_size_distribution")
distutils.dir_util.mkpath(output_dir + os.path.sep + "pics")

number_of_iterations = 100
chunk_size = 10000
def Split(reference_file):
    records = list(SeqIO.parse(reference_file, "fasta"))
    ref_record = records[0]
    for i in range(number_of_iterations):
        subsequence = ref_record.seq[i*chunk_size : i*chunk_size + chunk_size]
        base=os.path.basename(reference_file)
        filename = os.path.splitext(base)[0]
        outfilename = output_dir + os.path.sep + "split_ref" + os.path.sep + filename + "_" + str(i*chunk_size) + "_" + str(i*chunk_size + chunk_size) + ".fasta"
        record = SeqRecord(subsequence, id = ref_record.id + "_" + str(i*chunk_size) + "_" + str(i*chunk_size + chunk_size))
        SeqIO.write(record, outfilename, "fasta")

def Align():
    for filename in os.listdir(output_dir + os.path.sep + "split_ref"):
        if filename.endswith(".fasta"):
            call(["bwa", "index", output_dir + os.path.sep + "split_ref" + os.path.sep + filename])
            out=output_dir + os.path.sep + "sam_files" + os.path.sep  + os.path.splitext(filename)[0] + ".sam"
            with open(out, "w+") as f:
                call(["bwa", "mem", output_dir + os.path.sep + "split_ref" + os.path.sep + filename, left_reads_file, right_reads_file], stdout=f)
            out2=output_dir + os.path.sep + "is_size_distribution" + os.path.sep  + os.path.splitext(filename)[0] + ".is"
            with open(out2, "w+") as f:
                call(["python", "/Finn/meleshko/data/CYANO/GERW/WITH_PACBIO/PAL_15AUG08-1/MiSeq_/get_is/getinsertsize.py", out], stdout=f)
            call(["Rscript", "/Finn/meleshko/data/CYANO/GERW/WITH_PACBIO/PAL_15AUG08-1/MiSeq_/PAL_analysis/is_size_distribution/draw_pics.R", out2])
            call(["mv", "/Finn/meleshko/data/CYANO/GERW/WITH_PACBIO/PAL_15AUG08-1/MiSeq_/PAL_analysis/is_size_distribution/*.png", "/Finn/meleshko/data/CYANO/GERW/WITH_PACBIO/PAL_15AUG08-1/MiSeq_/PAL_analysis/pics/"])
#Split(reference_file)
Align()

