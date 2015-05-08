__author__ = 'Daniel'
import random

class Read(object):
    def __init__(self, start_index, size, data, error):
        self.start_index = start_index
        self.size = size
        self.data = [c if random.random() > error else ~c & 1 for c in data]
        self.flipped_data = [~c & 1 for c in self.data]

    def __repr__(self):
        result = ""
        for _ in range(0, self.start_index):
            result += " "
        for c in self.data:
            result += str(c)
        return result
