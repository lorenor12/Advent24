import os
from typing import Tuple, Any

import numpy as np
from numpy import ndarray, dtype

# part 1
file = 'list.txt'
data = np.loadtxt(file, dtype='int')
list1 = data[:, 0]
list2 = data[:, 1]
list1.sort()
list2.sort()
diff = np.abs(list1 - list2)
sum_diff = np.sum(diff)
print(sum_diff)

# part 2
sim_score = 0
list1_uniq, list1_count = np.unique(list1, return_counts=True)
list2_uniq, list2_count = np.unique(list2, return_counts=True)
min_idx = 0
for idx1, num1 in enumerate(list1_uniq):
    for idx2, num2 in enumerate(list2_uniq[min_idx:]):
        if num1 == num2:
            num_count1 = list1_count[idx1]
            num_count2 = list2_count[idx2 + min_idx]
            sim_score += num1 * num_count2 * num_count1
            min_idx = idx2
            break
print(sim_score)




def calculate_diff_sum(list1, list2):
    list1.sort()
    list2.sort()
    diff = np.abs(list1 - list2)
    sum_diff = np.sum(diff)
    return sum_diff



def get_lists(file: str) -> tuple[ndarray[Any, dtype[Any]], ndarray[Any, dtype[Any]]]:
    data = np.loadtxt(file, dtype='int')
    list1 = data[:, 0]
    list2 = data[:, 1]
    return list1, list2

if __name__ == '__main__':
    list1, list2 = get_lists('list.txt')
