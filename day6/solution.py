import numpy as np


def move(start: np.ndarray, map: np.ndarray) -> (int, int):
    dir_dic = {1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}
    dir_indicator = map[start[0]][start[1]]
    direction = dir_dic[dir_indicator]
    map[start[0]][start[1]] = -1
    while True:
        next_idx = start + direction
        next_tile = map[next_idx[0]][next_idx[1]]
        if next_tile != 5:
            map[next_idx[0]][next_idx[1]] = dir_indicator
            return np.array([next_idx[0], next_idx[1]])
        dir_indicator = dir_indicator + 1 if dir_indicator + 1 < 5 else 1
        direction = dir_dic[dir_indicator]


def print_map(map):
    line = ''
    for idx, i in enumerate(map.flatten()):
        if i == -1:
            i = 6
        if idx % 10 == 0:
            print(line)
            line = ''
            line += str(i)
        else:
            line += str(i)
    print(line)


def main():
    file = 'data.txt'
    with open(file) as f:
        lines = f.read().split()
    map = [[]]
    for idx, line in enumerate(lines):
        if line.find('^') != -1:
            start_idx = (idx, line.find('^'))
        line_map = []
        for c in line:
            if c == '.':
                line_map.append(0)
            elif c == '^':
                line_map.append(1)
            else:
                line_map.append(5)
        map.append(line_map)
    del map[0]
    map = np.array(map)
    start_idx = np.array(start_idx)
    while True:
        try:
            start_idx = move(start_idx, map)
        except IndexError:
            break

    move_count = abs(np.sum(map, where=map == -1))
    print(move_count)


if __name__ == '__main__':
    main()