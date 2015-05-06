__author__ = 'Daniel'

class Read(object):
    def __init__(self, start_index, size, data):
        self.start_index = start_index
        self.size = size
        self.data = list(data)
        self.flipped_data = []
        for c in self.data:
            self.flipped_data.append(~c & 1)

    def __repr__(self):
        result = ""
        for _ in range(0, self.start_index):
            result += " "
        for c in self.data:
            result += str(c)
        return result
