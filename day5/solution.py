

def is_valid(update: list[int], rules: dict[int, list[int]]) -> bool:
    for idx, page in enumerate(update[1:], 1):
        if page in rules.keys():
            for num in rules[page]:
                if num in update[:idx]:
                    return False
    return True


def get_relevant_rules(update: list[int], rules: dict[int, list[int]]) -> list[int]:
    relevant_rules = {}
    for page in rules.keys():
        if page in update:
            relevant_rules[page] = []
            for p in rules[page]:
                if p in update:
                    relevant_rules[page].append(p)
    return relevant_rules


def get_fixed_update(update: list[int], rules: dict[int, list[int]]) -> list[int]:
    fixed_update = []
    rules = get_relevant_rules(update, rules)

    missing_nums = len(update)
    sorted_keys = sorted(rules.keys(), key=lambda k: len(rules[k]))
    for key in sorted_keys:
        if not fixed_update or True:
            fixed_update.insert(0, key)


    return fixed_update

def main():
    # part 1
    with open('data.txt', 'r') as f:
        data = f.read()
    split_data = data.split('\n\n')
    str_updates = split_data[1].split('\n')
    updates = [list(map(int, str_update.split(','))) for str_update in str_updates]
    str_rules = split_data[0].split('\n')
    rules_list = [list(map(int, str_rule.split('|'))) for str_rule in str_rules]

    rules_dict = {}
    for rule in rules_list:
        if rule[0] in rules_dict.keys():
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]

    mid_sum = 0
    for update in updates:
        if is_valid(update, rules_dict):
            mid_sum += update[int(len(update)/2)]
    print(mid_sum)

    # part 2
    mid_sum = 0
    for update in updates:
        if is_valid(update, rules_dict):
            continue
        update = get_fixed_update(update, rules_dict)
        if not is_valid(update, rules_dict):
            print("error")
        mid_sum += update[int(len(update)/2)]
    print(mid_sum)




if __name__ == '__main__':
    main()