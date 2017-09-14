__author__ = 'dima'

ref_dir = "/Finn/meleshko/meta/son_summer_school/references"
reads_dir = "/Finn/meleshko/meta/son_summer_school/reads"
assembly_dir = "/Finn/meleshko/meta/son_summer_school/assemblies"
log_dir = "/Finn/meleshko/meta/son_summer_school/logs"

from os import listdir, path, system
from os.path import isfile, join
import random

onlyfiles = [ref_dir + "/" + f for f in listdir(ref_dir) if isfile(join(ref_dir, f))]


def CreateDataset(a):
    with open(log_dir + "/log.txt", 'a') as log, open(log_dir + "/answer.txt", 'a') as b:
        log.write(str(a) + ":\n")
        number_of_species = random.randint(1,10)
        b.write(str(number_of_species) + ":\n")
        species = random.sample(range(0, 10), number_of_species)
        coverages = random.sample(range(20, 300, 5), number_of_species)
        for i in range(0, len(species)):
            log.write(path.basename(onlyfiles[species[i]]) + " " + str(coverages[i]) + "\n")
            system("/home/dmeleshko/tools/art_bin_ChocolateCherryCake/art_illumina -f " + str(coverages[i]) + " -i " + onlyfiles[species[i]] + " -p -l 250 -m 500 -s 70 -o " + reads_dir + "/" + str(species[i]))
        system("cat >" + reads_dir + "/" + str(a) + "_1.fastq " + reads_dir + "/*1.fq" )
        system("cat >" + reads_dir + "/" + str(a) + "_2.fastq " + reads_dir + "/*2.fq" )

        system("rm " + reads_dir + "/*.fq" )
        system("rm " + reads_dir + "/*.aln" )








for i in range(0, 20):
    CreateDataset(i)