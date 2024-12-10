import numpy as np


def get_disk(disk_map: np.ndarray, ids: list[int]) -> np.ndarray:
    total_space = disk_map.sum()
    disk = np.ones(total_space, dtype=np.int32) * -2
    prev_idx = 0
    id_idx = 0
    for i in range(len(disk_map)):
        num_blocks = disk_map[i]
        if i % 2 == 1:
            curr_id = -1
        else:
            curr_id = ids[id_idx]
            id_idx += 1
        for j in range(num_blocks):
            disk[j + prev_idx] = curr_id
        if num_blocks != 0:
            prev_idx += j + 1
    return disk


def compress_disk(disk: np.ndarray) -> np.ndarray:
    rev_idx = 1
    disk_len = len(disk)
    for i in range(len(disk)):
        if (disk[i:] == -1).all():
            break
        if disk[i] == -1:
            while disk[disk_len - rev_idx] == -1:
                rev_idx += 1
            disk[i] = disk[disk_len - rev_idx]
            disk[disk_len - rev_idx] = -1
            rev_idx += 1
    return disk


def compress_disk_without_fragmentation(disk: np.ndarray) -> np.ndarray:
    rev_idx = 0
    disk_len = len(disk)
    rev_disk = disk[::-1]
    max_idx = disk_len
    max_idx_reverse = disk_len
    while rev_idx < max_idx:
        while rev_disk[rev_idx] == -1:
            rev_idx += 1
        file_block_size = 0
        file_id = rev_disk[rev_idx]
        # calculate file block size
        while rev_idx + file_block_size < max_idx and rev_disk[rev_idx + file_block_size] == file_id:
            file_block_size += 1

        # find fitting free space
        i = 0
        while i < max_idx:
            if disk[i] == -1:
                free_block_size = 0
                # calculate free block size
                while i + free_block_size < max_idx and disk[i + free_block_size] == -1:
                    free_block_size += 1

                if file_block_size <= free_block_size and i < disk_len - rev_idx:

                    disk[i:i + file_block_size] = rev_disk[rev_idx:rev_idx + file_block_size]
                    rev_disk[rev_idx:rev_idx + file_block_size] = -1
                    if -1 not in disk[:disk_len - (rev_idx + file_block_size)]:
                        max_idx = disk_len - (rev_idx + file_block_size)
                    break
                else:
                    i += free_block_size
            else:
                i += 1

        rev_idx += file_block_size
    return disk


def calculate_checksum(disk: np.ndarray) -> np.int64:
    checksum = np.int64(0)
    for i, file in enumerate(disk):
        if file != -1:
            checksum += i * file
    return checksum


def main():
    file = 'data.txt'
    with open(file) as f:
        data = f.read()
    disk_list = [int(c) for c in data]
    disk_map = np.array(disk_list)

    num_ids = int((len(disk_map) + 1) / 2)
    ids = [i for i in range(num_ids)]
    disk = get_disk(disk_map, ids)
    #disk = compress_disk(disk.copy())
    with open('dump.txt', 'w') as f:
        f.write(str(disk.tolist()))
    print(calculate_checksum(disk))
    disk = compress_disk_without_fragmentation(disk)
    with open('dump.txt', 'w') as f:
        f.write(str(disk.tolist()))
    print(calculate_checksum(disk))
    print(disk)






if __name__ == '__main__':
    main()