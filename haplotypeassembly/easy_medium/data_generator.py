__author__ = 'Daniel'
import random

from haplotypeassembly.easy_medium.read import Read


class DataGenerator(object):
    def __init__(self, size):
        '''
        Constructor
        '''
        self.size = size
        self.hap1 = []
        self.hap2 = []
        self.reads = []
        for _ in range(0, size / 25):
            chunk = random.getrandbits(25)
            for i in range(0, 25):
                choice = (chunk & (1 << i)) >> i
                self.hap1.append(choice)
                self.hap2.append(~choice & 1)

    def __repr__(self):
        result = ""
        for c in self.hap1:
            result += str(c)
        result += "\n"
        for c in self.hap2:
            result += str(c)
        return result

    def create_reads(self, min_size, max_size, min_distance, max_distance, error):
        if min_distance > max_distance or min_size > max_size:
            print "Error. Max must be >= min."
            return
        index = 0
        while index < self.size:
            read_size = random.randint(min_size, max_size)
            if random.random() < 0.5:
                data = self.hap1[index:index + read_size]
            else:
                data = self.hap2[index:index + read_size]
            read = Read(index, read_size, data, error)
            self.reads.append(read)
            index += min(random.randint(min_distance, max_distance), read_size - 1)


    @classmethod
    def print_haplotype(cls, haplotype):
        result = ""
        for c in haplotype:
            result += str(c)
        print result
