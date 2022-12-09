def create_lst():
    my_list = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            my_list.append(line)
    return my_list


def viewing_score(forest, r, c):
    if r == 0 or c == 0 or r == len(forest) - 1 or c == len(forest[0]) - 1:
        return 0

    row = r - 1

    up = 0
    while True:
        if row == -1:
            break
        up += 1
        if int(forest[row][c]) >= int(forest[r][c]):
            break
        row -= 1

    row = r + 1

    down = 0

    while True:
        if row == len(forest):
            break
        down += 1
        if int(forest[row][c]) >= int(forest[r][c]):
            break
        row += 1

    col = c - 1

    left = 0

    while True:
        if col == -1:
            break
        left += 1
        if int(forest[r][col]) >= int(forest[r][c]):
            break
        col -= 1

    col = c + 1

    right = 0
    while True:
        if col == len(forest[0]):
            break
        right += 1
        if int(forest[r][col]) >= int(forest[r][c]):
            break
        col += 1


    #print(up, left, right, down)
    return (up * left * right * down)


def main():
    
    forest = create_lst()

    max_scenic = 0
    for r in range(len(forest)):
        for c in range(len(forest[0])):
            if (answer:= viewing_score(forest, r, c)) > max_scenic:
                max_scenic = answer
    print(max_scenic)


if __name__ =="__main__":
    main()