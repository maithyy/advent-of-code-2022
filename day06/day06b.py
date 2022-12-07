def my_count(line):
    processed = 14
    my_list = list(line[:14])
    if len(my_list) == len(set(my_list)):
        return processed

    for letter in line[14:]:
        processed += 1
        del my_list[0]
        my_list.append(letter)
        if len(my_list) == len(set(my_list)):
            return processed

    

def main():
    with open('input.txt') as f:
        print(my_count(f.readline()))


if __name__ =="__main__":
    main()
    