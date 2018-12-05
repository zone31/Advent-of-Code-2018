#!/usr/bin/python3
import sys
from collections import Counter
#######################Helping functions###########################
def data_parser(filepath):
    """
    Parse the data by splitting each line into a string, and returning
    a generator for these strings
    """
    d = (line.rstrip() for line in open(filepath))
    return d
#########################Main functions############################
def solver_1star(d):
    """
    Use two counters, one for the total and one for each line.
    Collapse into a set of the most common observed lettes, and add
    this set to the total. Then look in the total counter and multiply the
    observations of 2 and 3 together.
    """
    total_count = Counter()
    for x in d:
        count = set((a for _,a in Counter(x).most_common()))
        total_count.update(count)
    return total_count[2]*total_count[3]

def solver_2star(d):
    """
    Iterate over the strings, compare each letter, and if they
    differ, note the position. If the position is over 0, it must
    have been set last iteration, so break the loop. If not, return
    the string
    """
    str_list = []
    for x in d:
        for y in str_list:
            pos = -1
            for count,data in enumerate(zip(x,y)):
                a,b = data
                if a != b:
                    if pos >= 0:
                        break
                    pos = count
            return x[:pos] + x[pos+1:]
        str_list.append(x)
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