NUM_ROWS = 9
TALLEST = 8

def create_list(lines):
    megalist = []
    for i in range(NUM_ROWS):
        megalist.append([])

    for line in reversed(lines):
        for i in range(1, NUM_ROWS * 4 - 2, 4):
            if line[i] != (" "):
                megalist[i//4].append(line[i])
    return megalist

def translate_move(line):
    line = line.rstrip().split()
    amount = int(line[1])
    start = int(line[3]) - 1
    end = int(line[5]) - 1
    
    return start, end, amount

def main():
    with open('input.txt') as f:
        muh_list = []
        for i in range(TALLEST):
            muh_list.append(f.readline().strip("\n"))
        crates = create_list(muh_list)
        f.readline()
        f.readline()

        for line in f:
            start, end, amount = translate_move(line)
            for _ in range(amount):
                crates[end].append(crates[start].pop(len(crates[start]) - 1))
        
        for i in range(len(crates)):
            for element in reversed(crates[i]):
                if (element != " "):
                    print(element, end="")
                    break


if __name__ =="__main__":
    main()
    