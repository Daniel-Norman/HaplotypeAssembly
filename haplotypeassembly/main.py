__author__ = 'Daniel'
from haplotypeassembly.easy_medium.data_generator import DataGenerator
from haplotypeassembly.hard.data_generator import  DataGeneratorHard
from haplotypeassembly.easy_medium.easy_assembler import EasyAssembler


def main():

    size = 100

    '''

    gen = DataGenerator(size)

    gen.create_reads(min_size=3, max_size=5, min_distance=0, max_distance=3, error=0.1)

    print "Generated data"
    print gen
    for read in gen.reads:
        print read

    hap = EasyAssembler.assemble_haplotype(gen.reads, size)
    print "Assembled data"
    DataGenerator.print_haplotype(hap)

    print "Original haps:"
    print gen

    '''

    genH = DataGeneratorHard(size)
    print genH

    genH.create_reads(min_size=8, max_size=10, min_distance=0, max_distance=1, error=0.2, overlap_chance=0.9)
    for read in genH.reads:
        print read



if __name__ == "__main__":
    main()



