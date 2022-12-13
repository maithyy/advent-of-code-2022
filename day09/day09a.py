ROWS = 5
COLS = 6
H = 1
T = 2
HT = 3

import numpy as np

def new_coord(r, c, dir):
    if dir == 'U':
        r -= 1
    elif dir == 'D':
        r += 1
    elif dir == 'L':
        c -= 1
    elif dir == 'R':
        c += 1
    return r, c


def touching(hr, hc, tr, tc):
    if hr - tr in [-1, 0, 1] and hc - tc in [-1, 0, 1]:
        return True

def diagonal(hr, hc, tr, tc):
    if hr-tr in [-1, 1] and hc-tc in [-1,1]:
        return True

def main():
    rope = np.zeros((ROWS, COLS))
    visited= np.zeros((ROWS, COLS))
    rope[ROWS-1][0] = HT
    visited[ROWS-1][0] = 1
    with open('input.txt') as f:
        hr = 4
        hc = 0
        tr = 4
        tc = 0
        for line in f:
            dir, move = line.rstrip().split()
            for _ in range(int(move)):
                rope[hr][hc] = 0
                new_hr, new_hc = new_coord(hr, hc, dir)
                if new_hr not in [0, 1, 2, 3, 4] or new_hc not in [0, 1, 2, 3, 4]:
                    visited[tr][tc] = visited[tr][tc] + 1
                else:
                    hr, hc = new_hr, new_hc
                    rope[hr][hc] = H
                    #print("rope")
                    #print(rope)
                    #print()
                    if not touching(hr, hc, tr, tc):
                        if hr-tr in [-2, 2]:
                            if hc > tc:
                                tc += 1
                            elif hc < tc:
                                tc -=1
                        elif hc-tc in [-2,2]:
                            if hr > tr:
                                tr += 1
                            elif hr < tr:
                                tr -=1
                        tr, tc = new_coord(tr, tc, dir)
                        rope[tr][tc] = T
                        visited[tr][tc] = visited[tr][tc] + 1
                    #print("visited")
                    #print(visited)
                    #print()
    print(visited)
    print(np.sum(visited))

if __name__ =="__main__":
    main()