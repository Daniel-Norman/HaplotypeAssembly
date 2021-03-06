__author__ = 'Daniel'
import random

class MediumAssembler:
    @classmethod
    def assemble_haplotype(cls, reads, size, overlap_requirement, match_requirement):
        corr_list = []
        haplotype_probs = [[0.0, 0.0] for _ in range(0, size)]
        setA = set()
        setB = set()
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
                        if len(setA) == 0:
                            setA.add(i)
                        if i in setA:
                            if j in setB:
                                setB.remove(j)
                                setA.remove(i)
                            else:
                                setA.add(j)
                        elif i in setB:
                            if j in setA:
                                setA.remove(j)
                                setB.remove(i)
                            else:
                                setB.add(j)
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
                j += 1
        setC = setA if len(setA) > len(setB) else setB
        for i in setC:
            read = reads[i]
            for j in range(0, read.size):
                haplotype_probs[read.start_index + j][0] += 1
                haplotype_probs[read.start_index + j][1] += read.data[j]

        haplotype = [0] * size
        guesses = 0
        for i in range(0, size):
            if haplotype_probs[i][0] == 0:
                haplotype[i] = random.choice([0, 1])
                guesses += 1
            elif haplotype_probs[i][1] / haplotype_probs[i][0] > 0.5:
                haplotype[i] = 1
            else:
                haplotype[i] = 0
        #print "Number of guesses:", guesses
        return haplotype





