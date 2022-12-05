def check_range(line):
    x, y = line.strip().split(",")
    x_start, x_end = x.split("-")
    y_start, y_end = y.split("-")
    x_start = int(x_start)
    x_end = int(x_end)
    y_start = int(y_start)
    y_end = int(y_end)

    if x_start < y_start: # y contained if it starts after x and ends before x
        return x_end >= y_end
    elif y_start < x_start:
        #x contained if it starts after y and ends before y
        return y_end >= x_end
    return True



def main():
    total = 0
    with open('input.txt') as f:
        for line in f:
            if check_range(line):
                total+= 1
    return total


if __name__ =="__main__":
    print(main())