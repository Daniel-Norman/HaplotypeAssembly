__author__ = 'Daniel'
from haplotypeassembly.easy_medium.data_generator import DataGenerator
from haplotypeassembly.hard.data_generator import DataGeneratorHard
from haplotypeassembly.easy_medium.easy_assembler import EasyAssembler
from haplotypeassembly.easy_medium.medium_assembler import MediumAssembler
import time

def main():

    easy_sd_sum = 0.0
    medium_sd_sum = 0.0
    reads_sum = 0.0
    num_trials = 50
    size = 1000
    sd_array = [0] * size

    for overlap_chance in range(0, 1):
        print "\nOverlap_chance:", overlap_chance / 20.0
        for k in range(0, num_trials):
            gen = DataGenerator(size)
            gen.create_reads(min_size=10, max_size=20, min_distance=0, max_distance=5, error=0.1, overlap_chance=0.8)
            hapE = EasyAssembler.assemble_haplotype(gen.reads, size)
            hapM = MediumAssembler.assemble_haplotype(reads=gen.reads, size=size, overlap_requirement=4, match_requirement=0.55)
            easy_sd_sum += min(switch_distance(hapE, gen.hap1), switch_distance(hapE, gen.hap2))
            medium_sd = min(switch_distance(hapM, gen.hap1), switch_distance(hapM, gen.hap2))
            medium_sd_sum += medium_sd
            reads_sum += len(gen.reads)
            sd_array[medium_sd] += 1
            #print k + 1

        print "Easy Avg SD:", easy_sd_sum / num_trials
        print "Medium Avg SD:", medium_sd_sum / num_trials
        print "Avg Number of reads:", reads_sum / num_trials


        for i in range(0, len(sd_array)):
            if sd_array[i] > 0:
                print i, sd_array[i]

        easy_sd_sum = 0.0
        medium_sd_sum = 0.0
        reads_sum = 0.0
        sd_array = [0] * size



    '''

    size = 1000


    gen = DataGenerator(size)

    gen.create_reads(min_size=10, max_size=20, min_distance=0, max_distance=5, error=0.1, overlap_chance=0.8)

    print "Generated data."
    print "Number of reads:", len(gen.reads)

    #for read in gen.reads:
        #print read

    #print "\nOriginal haps:"
    #print gen

    start = time.clock()
    hap = EasyAssembler.assemble_haplotype(gen.reads, size)
    end = time.clock()
    print "Assembled easy hap.", end - start
    print "\n\nEasy algorithm assembled data:"
    print_haplotype(hap)

    print "Switch distance:", min(switch_distance(hap, gen.hap1), switch_distance(hap, gen.hap2)), "\n"



    hapM = MediumAssembler.assemble_haplotype(gen.reads, size)
    print "\nMedium algorithm assembled data:"
    print_haplotype(hapM)
    print "Switch distance:", min(switch_distance(hapM, gen.hap1), switch_distance(hapM, gen.hap2))

    '''

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



