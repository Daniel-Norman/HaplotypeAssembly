__author__ = 'Daniel'
from haplotypeassembly.easy_medium.data_generator import DataGenerator
from haplotypeassembly.hard.data_generator import DataGeneratorHard
from haplotypeassembly.easy_medium.easy_assembler import EasyAssembler
from haplotypeassembly.easy_medium.medium_assembler import MediumAssembler
from haplotypeassembly.hard.hard_assembler import HardAssembler
import time

def main():
    p_haps = True
    p_reads = False

    size = 100
    gen = DataGenerator(size)
    if p_haps:
        print "Original Haplotypes:"
        print gen
    min_size = 10
    max_size = 20
    min_distance = 0
    max_distance = 5
    error = 0.15
    overlap_chance = 0.5
    gen.create_reads(min_size=min_size, max_size=max_size, min_distance=min_distance, max_distance=max_distance,
                     error=error, overlap_chance=overlap_chance)
    if p_reads:
        print "\nReads:"
        for read in gen.reads:
            print read

    print "\nTesting Easy Algorithm"
    easy_haplotype = EasyAssembler.assemble_haplotype(gen.reads, size)
    if p_haps:
        print "Assembled haplotypes:"
        print_haplotype(easy_haplotype, flipped=False)
        print_haplotype(easy_haplotype, flipped=True)
    print "Switch distance:"
    print min(switch_distance(easy_haplotype, gen.hap1), switch_distance(easy_haplotype, gen.hap2))

    print "\nTesting Medium Algorithm"
    overlap_requirement = 4
    match_requirement = 0.55
    medium_haplotype = MediumAssembler.assemble_haplotype(reads=gen.reads, size=size,
                                                          overlap_requirement=overlap_requirement,
                                                          match_requirement=match_requirement)
    if p_haps:
        print "Assembled haplotypes:"
        print_haplotype(medium_haplotype, flipped=False)
        print_haplotype(medium_haplotype, flipped=True)
    print "Switch distance:"
    print min(switch_distance(medium_haplotype, gen.hap1), switch_distance(medium_haplotype, gen.hap2))



def switch_distance(hap1, hap2):
    count = 0
    switch = 0
    for i in range(0, len(hap1)):
        if hap1[i] ^ hap2[i] ^ switch:
            count += 1
            switch = ~switch & 1
    return count

def print_haplotype(haplotype, flipped):
    result = ""
    if not flipped:
        for c in haplotype:
            result += str(c)
    else:
        for c in haplotype:
            if c == 0:
                result += "1"
            else:
                result += "0"
    print result

if __name__ == "__main__":
    main()



