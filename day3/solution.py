import re


# part 1
file = 'data.txt'
with open(file, 'r') as f:
    data = f.read()
    mults = re.findall('mul\(\d{1,3},\d{1,3}\)', data)
    numbers = [re.findall('\d{1,3}', mult) for mult in mults]
    mult_sum = sum([int(l[0]) * int(l[1]) for l in numbers])
    print(mult_sum)


# part 2
file = 'data.txt'
with open(file, 'r') as f:
    data = f.read()
    matches = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t', data)
    do = True
    mult_sum = 0
    for match in matches:
        if 'mul' in match and do:
            mults = re.findall('\d{1,3}', match)
            mult_sum += int(mults[0]) * int(mults[1])
        elif 'don\'t' in match:
            do = False
        elif 'do()' in match:
            do = True
    print(mult_sum)