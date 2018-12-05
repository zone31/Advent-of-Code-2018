#!/usr/bin/python3
import sys
from functools import reduce
#######################Helping functions###########################
def data_parser(filepath):
    """
    Parse the data by splitting each line into a string, and making
    each string into integers.
    """
    d = (line.rstrip() for line in open(filepath))
    return (int(s) for s in d)
#########################Main functions############################
def solver_1star(d):
    """
    Reduce the values in the generator, since the value is the sum
    of all values in the list.
    """
    return reduce((lambda x, y: x + y), d)

def solver_2star(d):
    """
    Loop the list until we find an result. Keep a set of already seen
    values, and compare if we already have seen them. If we have, return
    that value.
    """
    seen = set()
    accum = 0
    while True:
        for x in d:
            accum += x
            if accum in seen:
                return accum
            seen.add(accum)
##############################MAIN#################################
def main():
    """
    Run the program by itself, return a tuple of star1 and star2
    """
    input_soruce = "../input1.txt"
    # Make list, since the generator has to be used multiple times
    d = list(data_parser(input_soruce))
    return (solver_1star(d),solver_2star(d))

if __name__ == "__main__":
    star1,star2 = main()
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == '1':
           print(star1)
        elif arg == '2':
           print(star2)
    else:
        print("Day 1 first star:")
        print(star1)
        print("Day 1 second star:")
        print(star2)