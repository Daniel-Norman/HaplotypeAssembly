__author__ = 'Daniel'
import random

class DataGenerator(object):
    def __init__(self, size):
        '''
        Constructor
        '''
        self.size = size
        self.hap1 = []
        self.hap2 = []
        for _ in range(0, size):
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
