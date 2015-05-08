__author__ = 'Daniel'
import random

from haplotypeassembly.easy_medium.read import Read


class DataGeneratorHard(object):
    def __init__(self, size):
        '''
        Constructor
        '''
        self.size = size
        self.hap1 = []
        self.hap2 = []
        self.hap3 = []
        self.reads = []
        for _ in range(0, size / 25):
            chunk1 = random.getrandbits(25)
            chunk2 = random.getrandbits(25)
            chunk3 = random.getrandbits(25)
            for i in range(0, 25):
                self.hap1.append((chunk1 & (1 << i)) >> i)
                self.hap2.append((chunk2 & (1 << i)) >> i)
                self.hap3.append((chunk3 & (1 << i)) >> i)
        for i in range(size - 1, -1, -1):
            if self.hap1[i] == self.hap2[i] and self.hap1[i] == self.hap3[i]:
                self.hap1.pop(i)
                self.hap2.pop(i)
                self.hap3.pop(i)



    def __repr__(self):
        result = ""
        for c in self.hap1:
            result += str(c)
        result += "\n"
        for c in self.hap2:
            result += str(c)
        result += "\n"
        for c in self.hap3:
            result += str(c)
        return result

    def create_reads(self, min_size, max_size, min_distance, max_distance, error, overlap_chance):
        if min_distance > max_distance or min_size > max_size:
            print "Error. Max must be >= min."
            return
        index = 0
        while index < self.size:
            read_size = random.randint(min_size, max_size)
            choice = random.choice([1, 2, 3])
            if choice == 1:
                data = self.hap1[index:index + read_size]
            elif choice == 2:
                data = self.hap2[index:index + read_size]
            else:
                data = self.hap3[index:index + read_size]

            if len(data) > 0:
                read = Read(index, read_size, data, error)
                self.reads.append(read)
            if random.random() > overlap_chance:
                index += min(random.randint(min_distance, max_distance), read_size - 1)


    @classmethod
    def print_haplotype(cls, haplotype):
        result = ""
        for c in haplotype:
            result += str(c)
        print result
