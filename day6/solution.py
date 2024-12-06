from typing import Any

import numpy as np
from numpy import ndarray, dtype


def get_direction(start: np.ndarray, map: np.ndarray) -> (int, np.ndarray):
    dir_dic = {1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1]}
    dir_indicator = map[start[0]][start[1]]
    direction = dir_dic[dir_indicator]
    return dir_indicator, np.array(direction)


def rotate_direction(direction: np.ndarray) -> np.ndarray:
    rot_matrix = np.array([[0, -1], [1, 0]])
    rot_direction = np.dot(direction, rot_matrix)
    return rot_direction

def move(start: np.ndarray, map: np.ndarray, direction) -> (np.ndarray, np.ndarray):
    next_idx = start + direction
    curr_tile = map[start[0]][start[1]]
    try:
        if curr_tile > 0:
            curr_tile = -1
        else:
           curr_tile -= 1
    except ValueError:
        print("error")
    map[start[0]][start[1]] = curr_tile
    if curr_tile == -5:
        return None, None
    if next_idx[0] == -1 or next_idx[1] == -1:
        raise IndexError
    next_tile = map[next_idx[0]][next_idx[1]]
    if next_tile != 5:
        return np.array([next_idx[0], next_idx[1]]), direction
    else:
        direction = rotate_direction(direction)
        return start, direction


def is_guard_stuck(start_pos, map, direction):
    while True:
        try:
            if start_pos is None:
                return True
            start_pos, direction = move(start_pos, map, direction)
        except IndexError:
            return False


def find_possible_obstacle_positions(start_pos, map):
    obstacle_positions = []
    curr_pos = start_pos.copy()
    start_map = map.copy()
    prev_pos = np.array([0, 0])
    dir_indicator, direction = get_direction(curr_pos, map)
    start_direction = direction.copy()
    try:
        while True:
            # check that the guard moved.
            if prev_pos[0] != curr_pos[0] or prev_pos[1] != curr_pos[1] or True:
                rot_direction = rotate_direction(direction)
                next_pos = curr_pos + rot_direction
                next_tile = map[next_pos[0], next_pos[1]]
                obstacle_pos = curr_pos + direction
                # check that the next tile was already encountered
                if obstacle_pos.tolist() not in obstacle_positions:
                    if next_tile == -1 or True:
                        temp_map = start_map.copy()
                        temp_map[obstacle_pos[0], obstacle_pos[1]] = 5
                        if is_guard_stuck(start_pos, temp_map, start_direction):
                            obstacle_positions.append(obstacle_pos.tolist())
            prev_pos = curr_pos.copy()
            curr_pos, direction = move(curr_pos, map, direction)
    except IndexError:
        return obstacle_positions

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
                raise ValueError("invalid char in map input.")
        if idx == 0:
            map = [line_map]
        else:
            map.append(line_map)
    map = np.array(map)
    start_idx = np.array(start_idx)

    obstacle_positions = find_possible_obstacle_positions(start_idx.copy(), map.copy())
    dir_indicator, direction = get_direction(start_idx, map)
    while True:
        try:
            start_idx, direction = move(start_idx, map, direction)
            if start_idx is None:
                raise ValueError("Invalid Map.")
        except IndexError:
            break


    move_count = abs(np.sum(map, where=map == -1))
    print(obstacle_positions)
    print(len(obstacle_positions))
    print(move_count)


if __name__ == '__main__':
    main()