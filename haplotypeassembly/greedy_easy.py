__author__ = 'Daniel'
class GreedyEasy:

    @classmethod
    def assemble_haplotype(cls, reads, size):
        haplotype = [0] * size
        haplotype_index = 0
        read_index = 0
        while haplotype_index < size:
            while read_index < len(reads) - 1 and reads[read_index + 1].start_index < haplotype_index:
                read_index += 1
            read = reads[read_index]

            if haplotype_index > 0 and read.data[0] != haplotype[read.start_index]:
                haplotype[haplotype_index:read.start_index + read.size] = list(read.flipped_data[haplotype_index - read.start_index:])
            else:
                haplotype[haplotype_index:read.start_index + read.size] = list(read.data[haplotype_index - read.start_index:])

            haplotype_index += read.size - (haplotype_index - read.start_index)

        return haplotype

