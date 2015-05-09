__author__ = 'Daniel'
from haplotypeassembly.easy_medium.data_generator import DataGenerator
from haplotypeassembly.hard.data_generator import DataGeneratorHard
from haplotypeassembly.easy_medium.easy_assembler import EasyAssembler
from haplotypeassembly.easy_medium.medium_assembler import MediumAssembler


def main():

    size = 500

    gen = DataGenerator(size)

    gen.create_reads(min_size=5, max_size=10, min_distance=0, max_distance=1, error=0.1, overlap_chance=0.8)

    print "Generated data."

    #for read in gen.reads:
        #print read

    print "\nOriginal haps:"
    print gen

    hap = EasyAssembler.assemble_haplotype(gen.reads, size)
    print "\n\nEasy algorithm assembled data:"
    print_haplotype(hap)

    print "Switch distance:", min(switch_distance(hap, gen.hap1), switch_distance(hap, gen.hap2)), "\n"

    hapM = MediumAssembler.assemble_haplotype(gen.reads, size)
    print "\nMedium algorithm assembled data:"
    print_haplotype(hapM)
    print "Switch distance:", min(switch_distance(hapM, gen.hap1), switch_distance(hapM, gen.hap2))

    '''

    genH = DataGeneratorHard(size)
    print genH

    genH.create_reads(min_size=8, max_size=10, min_distance=0, max_distance=1, error=0.2, overlap_chance=0.9)
    for read in genH.reads:
        print read


    '''

def switch_distance(hap1, hap2):
    count = 0
    switch = 0
    for i in range(0, len(hap1)):
        if hap1[i] ^ hap2[i] ^ switch:
            count += 1
            switch = ~switch & 1
    return count

def print_haplotype(haplotype):
    result = ""
    for c in haplotype:
        result += str(c)
    print result


if __name__ == "__main__":
    main()



