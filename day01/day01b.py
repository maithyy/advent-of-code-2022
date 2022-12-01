def main():
    maximum = [0, 0, 0] #lowest to biggest
    total = 0

    with open('input.txt') as f:
        for line in f:
            if (line == "\n"):
                for index, element in enumerate(maximum):
                    if total > element:
                        maximum[index] = total
                        break
                total = 0
                maximum.sort()
            else:
                total += int(line)

    if total > element:
        maximum[index] = total
    
    return sum(maximum)

if __name__ == "__main__":
    print(main())