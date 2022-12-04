import math

def get_common(lineA, lineB, lineC):
    lineA = set(lineA.strip())
    lineB = set(lineB.strip())
    lineC = set(lineC.strip())
    result = lineA.intersection(lineB, lineC)
    return result.pop()

def main():
    letter_dict = {
        "a": 1, 
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }

    with open('input.txt') as f:
        total = 0
        while True:
            try:
                lineA = f.readline()
                lineB = f.readline()
                lineC = f.readline()
                answer = get_common(lineA, lineB, lineC)
                if answer.isupper():
                    total += letter_dict[answer.lower()] + 26
                else:
                    total += letter_dict[answer]
            except:
                return total

if __name__ =="__main__":
    print(main())