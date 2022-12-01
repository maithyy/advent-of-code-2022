def main():
    maximum = 0
    total = 0

    with open('input.txt') as f:
        for line in f:
            if (line == "\n"):
                if total > maximum:
                    maximum = total
                total = 0
            else:
                total += int(line)

    if total > maximum:
        maximum = total
    
    return maximum

if __name__ == "__main__":
    print(main())