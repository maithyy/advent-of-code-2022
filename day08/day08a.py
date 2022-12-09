def create_lst():
    my_list = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            my_list.append(line)
    return my_list

def get_visible(forest):
    visible = 0
    for r in range(len(forest)):
        for c in range(len(forest[0])):
            if check_valid(forest, r, c):
                visible += 1
    return visible


def check_valid(forest, r, c):
    if r == 0 or c == 0 or r == len(forest) or c == len(forest[0]):
        return True
    row = 0
    col = 0

    visible = True
    while row != r: # checks if visible from top
        if int(forest[row][c]) >= int(forest[r][c]):
            visible = False
            break
        row += 1
    if visible: return True

    visible = True
    while col != c: # checks if visible from left
        if int(forest[r][col]) >= int(forest[r][c]):
            visible = False
            break
        col += 1
    if visible: return True

    row, col = len(forest) - 1, len(forest[0]) - 1
    visible = True

    while row != r: # checks if visible from bot
        if int(forest[row][c]) >= int(forest[r][c]):
            visible = False
            break
        row -= 1
    if visible: return True

    visible = True
    while col != c: # checks if visible from right
        if int(forest[r][col]) >= int(forest[r][c]):
            visible = False
            break

        col -= 1
    if visible: return True

    return False


def main():
    my_list = create_lst()
    print(get_visible(my_list))


if __name__ =="__main__":
    main()