def points(line: str):
    """in the format of A Y"""
    my_dict = {"A": 1,"X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    opponent = my_dict[line[0]]
    you = my_dict[line[2]]

    if opponent == you:
        return you + 3
    elif opponent == 1: # if rock, win paper
        return you + 6 if you == 2 else you
    elif opponent == 2: # if paper win, scissors
        return you + 6 if you == 3 else you
    else: # if scissors, win rock
        return you + 6 if you == 1 else you

def main():
    with open('input.txt') as f:
        return sum(points(line) for line in f)

if __name__ =="__main__":
    print(main())