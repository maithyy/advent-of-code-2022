

def main():
    with open('input.txt') as f:
        cycle = 1
        value = 1
        total = 0
        for line in f:
            line = line.rstrip()
            if cycle in [20, 60, 100, 140, 180, 220]:
                total += (cycle * value)
            cycle += 1
            if line != "noop":
                if cycle in [20, 60, 100, 140, 180, 220]:
                    total += (cycle * value)
                value += int(line.split()[1])
                cycle += 1
        print(total)


if __name__ =="__main__":
    main()