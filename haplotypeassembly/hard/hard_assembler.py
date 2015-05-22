__author__ = 'Daniel'
import random

class HardAssembler:
    @classmethod
    def assemble_haplotype(cls, reads, size, overlap_requirement, match_requirement):
        corr_list = []
        setA = set()
        setB = set()
        setC = set()
        for i in range(0, len(reads)):
            read1 = reads[i]
            j = i + 1
            corr_list.append([])
            while j < len(reads) and read1.start_index + read1.size > reads[j].start_index:
                read2 = reads[j]

                count = 0.0
                matches = 0
                for k in range(read2.start_index, min(read1.start_index + read1.size, read2.start_index + read2.size)):
                    if read2.data[k - read2.start_index] == read1.data[k - read1.start_index]:
                        matches += 1
                    count += 1
                if count > overlap_requirement:
                    if matches / count > match_requirement:
                        if len(setA) == 0 and i not in setB and i not in setC:
                            setA.add(i)
                        elif len(setB) == 0 and i not in setA and i not in setC:
                            setB.add(i)
                        elif len(setC) == 0 and i not in setA and i not in setB:
                            setC.add(i)
                        if i in setA:
                            if j in setB:
                                setB.remove(j)
                                setA.remove(i)
                            elif j in setC:
                                setC.remove(j)
                                setA.remove(i)
                            else:
                                setA.add(j)
                        if i in setB:
                            if j in setA:
                                setA.remove(j)
                                setB.remove(i)
                            elif j in setC:
                                setC.remove(j)
                                setB.remove(i)
                            else:
                                setB.add(j)
                        if i in setC:
                            if j in setA:
                                setA.remove(j)
                                setC.remove(i)
                            elif j in setB:
                                setB.remove(j)
                                setC.remove(i)
                            else:
                                setC.add(j)
                    '''
                    if matches / count < (1 - match_requirement):
                        if len(setA) == 0:
                            setA.add(i)
                        if i in setA:
                            if j in setA:
                                setA.remove(j)
                                setA.remove(i)
                            else:
                                setB.add(j)
                        elif i in setB:
                            if j in setB:
                                setB.remove(j)
                                setB.remove(i)
                            else:
                                setA.add(j)
                    '''
                j += 1

        haplotype_probs_a = [[0.0, 0.0] for _ in range(0, size)]
        haplotype_probs_b = [[0.0, 0.0] for _ in range(0, size)]
        haplotype_probs_c = [[0.0, 0.0] for _ in range(0, size)]

        for i in setA:
            read = reads[i]
            for j in range(0, read.size):
                haplotype_probs_a[read.start_index + j][0] += 1
                haplotype_probs_a[read.start_index + j][1] += read.data[j]
        for i in setB:
            read = reads[i]
            for j in range(0, read.size):
                haplotype_probs_b[read.start_index + j][0] += 1
                haplotype_probs_b[read.start_index + j][1] += read.data[j]
        for i in setC:
            read = reads[i]
            for j in range(0, read.size):
                haplotype_probs_c[read.start_index + j][0] += 1
                haplotype_probs_c[read.start_index + j][1] += read.data[j]

        haplotype_a = [2] * size
        for i in range(0, size):
            if haplotype_probs_a[i][0] != 0:
                if haplotype_probs_a[i][1] / haplotype_probs_a[i][0] > 0.5:
                    haplotype_a[i] = 1
                else:
                    haplotype_a[i] = 0
        haplotype_b = [2] * size
        for i in range(0, size):
            if haplotype_probs_b[i][0] != 0:
                if haplotype_probs_b[i][1] / haplotype_probs_b[i][0] > 0.5:
                    haplotype_b[i] = 1
                else:
                    haplotype_b[i] = 0
        haplotype_c = [2] * size
        for i in range(0, size):
            if haplotype_probs_c[i][0] != 0:
                if haplotype_probs_c[i][1] / haplotype_probs_c[i][0] > 0.5:
                    haplotype_c[i] = 1
                else:
                    haplotype_c[i] = 0
        for i in range(0, size):
            if haplotype_a[i] == 2 and haplotype_b[i] != 2 and haplotype_b[i] == haplotype_c[i]:
                haplotype_a[i] = ~haplotype_b[i]
            if haplotype_b[i] == 2 and haplotype_a[i] != 2 and haplotype_a[i] == haplotype_c[i]:
                haplotype_b[i] = ~haplotype_a[i]
            if haplotype_c[i] == 2 and haplotype_a[i] != 2 and haplotype_a[i] == haplotype_b[i]:
                haplotype_c[i] = ~haplotype_a[i]

        guesses = 0
        #print "Number of guesses:", guesses
        return haplotype_a, haplotype_b, haplotype_c





