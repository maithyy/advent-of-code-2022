def check_range(line):
    x, y = line.strip().split(",")
    x_start, x_end = x.split("-")
    y_start, y_end = y.split("-")
    x_start = int(x_start)
    x_end = int(x_end)
    y_start = int(y_start)
    y_end = int(y_end)

    if x_start < y_start: # if x starts before y, make sure it ends before y
        return x_end < y_start
    elif y_start < x_start:
        return y_end < x_start
    return False



def main():
    total = 0
    with open('input.txt') as f:
        for line in f:
            if not check_range(line):
                total+= 1
    return total


if __name__ =="__main__":
    print(main())