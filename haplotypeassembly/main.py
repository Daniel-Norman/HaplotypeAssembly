__author__ = 'Daniel'
from data_generator import DataGenerator


def main():

    gen = DataGenerator(10000000 / 25)

    print len(gen.hap1)
    #print gen


if __name__ == "__main__":
    main()



