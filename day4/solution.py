

# part 1
file = 'data.txt'
with open(file, 'r') as f:
    lines = f.read().split('\n')
    close_idx = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1], [1, -1]]
    word = 'XMAS'
    num_word = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == word[0]:
                for idxs in close_idx:
                    found = False
                    next_i = i + idxs[0]
                    next_j = j + idxs[1]
                    for c in word[1:]:
                        if 0 <= next_i < len(lines) and 0 <= next_j < len(lines[next_i]):
                            if lines[next_i][next_j] == c:
                                found = True
                                next_i += idxs[0]
                                next_j += idxs[1]
                            else:
                                found = False
                                break
                        else:
                            found = False
                    if found:
                        num_word += 1

    print(num_word)

# part 2
file = 'data.txt'
with (open(file, 'r') as f):
    lines = f.read().split('\n')
    close_idx = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
    word = 'MS'
    num_word = 0
    num_found = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'A':
                word = 'MS'
                found = False
                for n, idx in enumerate(close_idx):
                    next_i = i + idx[0]
                    next_j = j + idx[1]
                    if n == 2:
                        word = 'MS'
                    if 0 <= next_i < len(lines) and 0 <= next_j < len(lines[next_i]):
                        if lines[next_i][next_j] in word:
                            word = 'S' if lines[next_i][next_j] == 'M' else 'M'
                            if n == 3:
                                num_word += 1
                        else:
                            break
                    else:
                        break

print(num_word)