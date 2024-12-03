from math import copysign


# part 1
file = 'data.txt'
num_safe_reports = 0
with open(file, 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        report = [int(num) for num in line.split()]
        growth = 0
        for i, n in enumerate(report[1:], 1):
            diff = n - report[i - 1]
            if 0 < abs(diff) < 4:
                if growth == 0:
                    growth = copysign(1, diff)
                elif copysign(1, diff) != growth:
                    num_safe_reports -= 1
                    break
            else:
                num_safe_reports -= 1
                break
        num_safe_reports += 1

print(num_safe_reports)


# part 2

def check_report(r: list) -> tuple[bool, int]:
    growth = 0
    for i, n in enumerate(r[1:], 1):
        diff = n - r[i - 1]
        if 0 < abs(diff) < 4:
            if growth == 0:
                growth = copysign(1, diff)
            elif copysign(1, diff) != growth:
                return False, i
        else:
            return False, i
    return True, i


file = 'data.txt'
num_safe_reports = 0
with open(file, 'r') as f:
    lines = f.read().split('\n')
    for line in lines:
        report = [int(num) for num in line.split()]
        safe, idx = check_report(report)
        if not safe:
            new_report = report[:idx] + report[idx+1:]
            safe, temp_idx = check_report(new_report)
        if not safe:
            new_report = report[:idx-1] + report[idx:]
            safe, temp_idx = check_report(new_report)
        if not safe:
            new_report = report[:0] + report[1:]
            safe, temp_idx = check_report(new_report)
        if safe:
            num_safe_reports += 1

print(num_safe_reports)


