

def find_path(puzzle: list[list[int]], cursor: list[int], nines=None, distinct=False) -> int:
    height = puzzle[cursor[0]][cursor[1]]
    puzzle_dims = (len(puzzle), len(puzzle[0]))
    if nines is None:
        nines = []
    if height == 9:
        if not distinct or cursor not in nines:
            nines.append(cursor)
    if cursor[0] > 0 and puzzle[cursor[0] - 1][cursor[1]] == height + 1:
        find_path(puzzle, [cursor[0] - 1, cursor[1]], nines, distinct)
    if cursor[0] < puzzle_dims[0] - 1 and puzzle[cursor[0] + 1][cursor[1]] == height + 1:
        find_path(puzzle, [cursor[0] + 1, cursor[1]], nines, distinct)
    if cursor[1] > 0 and puzzle[cursor[0]][cursor[1] - 1] == height + 1:
        find_path(puzzle, [cursor[0], cursor[1] - 1], nines, distinct)
    if cursor[1] < puzzle_dims[1] - 1 and puzzle[cursor[0]][cursor[1] + 1] == height + 1:
        find_path(puzzle, [cursor[0], cursor[1] + 1], nines, distinct)
    return nines

def main():
    file = 'data.txt'
    with open(file) as f:
        lines = f.read().split('\n')
    puzzle = []
    for line in lines:
        data = [int(c) for c in line]
        puzzle.append(data)
    zeros = []
    for i, row in enumerate(puzzle):
        for j, num in enumerate(row):
            if num == 0:
                zeros.append([i, j])

    num_paths = 0
    for zero in zeros:
        temp = find_path(puzzle, zero, distinct=True)
        num_paths += len(temp)
        #print(temp)
    print(num_paths)

    num_paths = 0
    for zero in zeros:
        temp = find_path(puzzle, zero, distinct=False)
        num_paths += len(temp)
        #print(temp)
    print(num_paths)



if __name__ == '__main__':
    main()