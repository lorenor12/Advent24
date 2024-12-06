import numpy as np


def get_direction(start, map):
    dir_dic = {1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}
    dir_indicator = map[start[0]][start[1]]
    direction = dir_dic[dir_indicator]
    return dir_indicator, direction


def move(start: np.ndarray[int], map: np.ndarray[int, int]) -> np.ndarray[int]:
    dir_indicator, direction = get_direction(start, map)
    next_idx = start + direction
    if next_idx[0] == -1 or next_idx[1] == -1:
        raise IndexError
    next_tile = map[next_idx[0]][next_idx[1]]
    map[start[0]][start[1]] = -1
    if next_tile != 5:
        map[next_idx[0]][next_idx[1]] = dir_indicator
        return np.array([next_idx[0], next_idx[1]])
    else:
        dir_indicator = (dir_indicator % 4) + 1
        map[start[0]][start[1]] = dir_indicator
        return start


def print_map(map):
    line = ''
    for idx, i in enumerate(map.flatten()):
        if i == -1:
            i = 'X'
        elif i == 0:
            i = '.'
        elif i == 5:
            i = '#'
        if idx % map.shape[0] == 0:
            print(line)
            line = ''
            line += str(i)
        else:
            line += str(i)
    print(line)

def save_map(map):
    shape = map.shape
    with open('dump.txt', 'w') as f:
        for i in range(shape[0]):
            for j in range(map.shape[1]):
                j = map[i, j]
                if j == -1:
                    j = 'X'
                elif j == 0:
                    j = '.'
                elif j == 5:
                    j = '#'
                elif j == 1:
                    j = '^'
                f.write(j)
            f.write('\n')



def main():
    file = 'data.txt'
    with open(file) as f:
        lines = f.read().split()
    map = []
    for idx, line in enumerate(lines):
        if line.find('^') != -1:
            start_idx = (idx, line.find('^'))
        line_map = []
        for c in line:
            if c == '.':
                line_map.append(0)
            elif c == '^':
                line_map.append(1)
            elif c == '#':
                line_map.append(5)
            else:
                raise ValueError
        if idx == 0:
            map = [line_map]
        else:
            map.append(line_map)
    map = np.array(map)
    save_map(map)
    start_idx = np.array(start_idx)
    count = 0
    while True:
        count += 1
        try:
            start_idx = move(start_idx, map)
        except IndexError:
            break

    move_count = abs(np.sum(map, where=map == -1))
    print(move_count)


if __name__ == '__main__':
    main()