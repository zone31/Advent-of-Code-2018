#!/usr/bin/python3
import sys
from collections import Counter
#######################Helping functions###########################
def data_parser(filepath):
    """
    Parse the data by splitting each line into a string, then parsing
    the string and representing the id, position, height and width in
    a tuple for that line
    """
    data = []
    for line in (a.rstrip() for a in open(filepath)):
        print
        comp = line.split(" ")
        cloth_id = int(comp[0][1:])
        pos = tuple(map(int,comp[2][:-1].split(",")))
        dim = tuple(map(int,comp[3].split("x")))
        data.append((cloth_id,pos,dim))
    return data
#########################Main functions############################
def solver_1star(d):
    """
    Set up a dict with the coordinates of the fabrics, when a piece
    of cloth is placed, add the area to the map. When done, count
    each area where more than one overlap
    """
    fabric = dict()
    for _,pos,dim in d:
        x,y = pos
        height,width = dim
        # Iterate over the coordinates represented by the cloth
        for xd in range(x,x+height):
            for yd in range(y,y+width):
                coord = (xd,yd)
                if coord in fabric:
                    fabric[coord] += 1
                else:
                    fabric[coord] = 1
    overlap = {k: v for k, v in fabric.items() if v > 1}
    return len(overlap)

def solver_2star(d):
    """
    Do as in the first star, but keep a set of already observed IDs.
    Subtract with this set for each visited area, and return this element
    in the end.
    """
    fabric = dict()
    special_cloth = set()
    for cloth_id,pos,dim in d:
        x,y = pos
        height,width = dim
        special_cloth.add(cloth_id)
        for xd in range(x,x+height):
            for yd in range(y,y+width):
                coord = (xd,yd)
                if coord in fabric:
                    fabric[coord].add(cloth_id)
                    special_cloth -= fabric[coord]
                else:
                    fabric[coord] = set([cloth_id])
    return special_cloth.pop()
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