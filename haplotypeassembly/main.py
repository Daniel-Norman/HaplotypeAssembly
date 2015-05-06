__author__ = 'Daniel'
from data_generator import DataGenerator
from greedy_easy import GreedyEasy


def main():

    size = 100
    gen = DataGenerator(size)

    gen.create_reads(min_size=4, max_size=10, min_distance=0, max_distance=3)

    print gen
    for read in gen.reads:
        print read


    hap = GreedyEasy.assemble_haplotype(gen.reads, size)

    DataGenerator.print_haplotype(hap)

if __name__ == "__main__":
    main()



