def points(line: str):
    """in the format of A Y"""
    my_dict = {"A": 1,"X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
    opponent = my_dict[line[0]]
    you = my_dict[line[2]]

    if you == 2: #draw
        return opponent + 3
    elif you == 1: #lose
        if opponent == 1:
            return 3
        elif opponent == 2:
            return 1
        else:
            return 2
    else:
        if opponent == 1:
            return 2 + 6
        elif opponent == 2:
            return 3 + 6
        else:
            return 1 + 6


def main():
    with open('input.txt') as f:
        return sum(points(line) for line in f)

if __name__ =="__main__":
    print(main())