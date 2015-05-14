__author__ = 'Daniel'
import random

class Read(object):
    def __init__(self, start_index, data, error):
        self.start_index = start_index
        self.data = [c if error == 0 or random.random() > error else random.choice([0, 1]) for c in data]
        self.size = len(self.data)
        self.flipped_data = [~c & 1 for c in self.data]

    def __repr__(self):
        result = ""
        for _ in range(0, self.start_index):
            result += " "
        for c in self.data:
            result += str(c)
        return result
