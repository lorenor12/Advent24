from typing import List, Any


def get_operators(result: int, numbers: list[int], operators=None, curr_operators=None, use_concat=True)\
        -> list[str] | None:
    possible_operators = ['*', '+', '||']
    if operators is None:
        operators = []
    if curr_operators is None:
        curr_operators = []

    if len(numbers) == 1:
        if numbers[0] == result:
            operators.append(curr_operators)
    else:
        for op in possible_operators:
            loop_operators = curr_operators.copy()
            if op == '*':
                left_over = result / numbers[-1]
            elif op == '+':
                left_over = result - numbers[-1]
            elif op == '||' and use_concat:
                str_result = str(result)
                str_num = str(numbers[-1])
                len_result = len(str_result)
                len_num = len(str_num)
                to_remove = str_result[len_result-len_num:]
                if to_remove == str_num and len_num != len_result:
                    str_left_over = str_result[:len(str_result)-len(str_num)]
                    left_over = int(str_left_over)
                else:
                    continue
            if float(left_over).is_integer() and left_over > 0:
                loop_operators.append(op)
                get_operators(int(left_over), numbers[:-1], operators, loop_operators)
    return operators


def get_operators_forward(result: int, numbers: list[int], operators=None, curr_operators=None, use_concat=True)\
        -> list[str] | None:
    possible_operators = ['*', '+', '||']
    if operators is None:
        operators = []
    if curr_operators is None:
        curr_operators = []

    if len(numbers) == 1:
        if numbers[0] == result:
            operators.append(curr_operators)
    else:
        for op in possible_operators:
            loop_operators = curr_operators.copy()
            if op == '*':
                temp_result = numbers[0] * numbers[1]
            elif op == '+':
                temp_result = numbers[0] + numbers[1]
            elif op == '||' and use_concat:
                str_result = str(numbers[0]) + str(numbers[1])
                temp_result = int(str_result)
                if not float(temp_result).is_integer():
                    raise ValueError()
            next_nums = [temp_result] + numbers[2:]
            loop_operators.append(op)
            get_operators_forward(result, next_nums, operators, loop_operators)
    return operators



def main():
    file = 'data.txt'
    with open(file) as f:
        lines = f.read().split('\n')
    equations = {}
    for line in lines:
        result, nums = line.split(': ')
        nums = [int(num) for num in nums.split(' ')]
        equations[int(result)] = nums
    total_calibration_result = 0
    past_num = 0
    for key in equations.keys():
        operators = get_operators_forward(key, equations[key])
        #print(operators)
        if len(operators) > 0:
            past_num = total_calibration_result
            total_calibration_result += key
            if past_num > total_calibration_result:
                raise ValueError()
    print(total_calibration_result)


if __name__ == '__main__':
    main()