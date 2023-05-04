import common
import random
import sys

def generate_random_numbers(list_length):
    return map(
      lambda x: random.randint(common.MIN_NUMBER, common.MAX_NUMBER),
      range(list_length))


def generate_all_numbers_of_digits1():
    return range(max([0, common.MIN_NUMBER]),
                 min([9, common.MAX_NUMBER]) + 1)


def generate_all_numbers_of_digits2():
    return range(max([10, common.MIN_NUMBER]),
                 min([99, common.MAX_NUMBER]) + 1)


def generate_all_numbers_of_digits3():
    return range(max([100, common.MIN_NUMBER]),
                 min([999, common.MAX_NUMBER]) + 1)


def duplicate_numbers(numbers, count):
    output_list = []
    indices = range(count)
    for value in numbers:
        for index in indices:
            output_list.append(value)
    return output_list


def numbers_to_string(numbers):
    return common.SERIALIZE_ITEM_DELIMETER.join(map(str, numbers))


def print_numbers(numbers):
    print numbers_to_string(numbers)


def save_numbers(file_name, numbers):
    with open(file_name, 'w') as f:
        f.write(numbers_to_string(numbers))


def parse_input():
    if len(sys.argv) == 2:
        list_length_arg = sys.argv[1]
        if common.is_numeric(list_length_arg):                
            return int(list_length_arg)
    msg = '''Usage:
    'python generate_numbers.py arg'
        where arg - list length
'''
    print msg
    raise common.CommandLineError()


if __name__ == '__main__':
    list_length = parse_input()
    numbers = generate_random_numbers(list_length)#duplicate_numbers(generate_all_numbers_of_digits1(), 3) #list_length)
    print_numbers(numbers)

