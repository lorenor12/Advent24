from multiprocessing import Pool
from typing import Tuple

import numpy as np
from numpy import ndarray


def blink(stones: list[int]) -> list[int]:
    i = 0
    while i < len(stones):
        stone = stones[i]

        if stone == 0:
            stones[i] = 1
        elif len(str(stone)) % 2 == 0:
            idx = int(len(str(stone)) / 2)
            new_stone1 = int(str(stone)[:idx])
            new_stone2 = int(str(stone)[idx:])
            stones[i] = new_stone2
            stones.insert(i + 1, new_stone1)
            i += 1
        else:
            stones[i] = stone * 2024
        i += 1
    return stones


def blink_no_duplicates(stones_dict: dict[int]) -> dict[int]:
    old_stones_dict = stones_dict.copy()
    new_stones_dict= {}
    for stone, occ in old_stones_dict.items():
        new_stones = blink([stone])
        for new_stone in new_stones:
            if new_stone in new_stones_dict.keys():
                new_stones_dict[new_stone] += occ
            else:
                new_stones_dict[new_stone] = occ
    return new_stones_dict


def main():
    # remove duplicates.
    file = 'data.txt'
    with open(file) as f:
        data = f.read().split(' ')
    stones = [int(d) for d in data]
    stones_dict = {}
    for stone in stones:
        stones_dict[stone] = 1
    for i in range(75):
        stones_dict = blink_no_duplicates(stones_dict)
    length = 0
    for val in stones_dict.values():
        length += val
    print(length)




if __name__ == '__main__':
    main()