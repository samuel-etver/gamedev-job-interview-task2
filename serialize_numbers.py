import common
import sys


def serialize(text):
    result_text = serialize_text(text)
    print(result_text)


def serialize_value(value):
    digit0 = value % common.SERIALIZE_POS0_TABLE_SIZE
    digit1 = value / common.SERIALIZE_POS0_TABLE_SIZE
    char0 = common.SERIALIZE_POS0_TABLE[digit0]
    if digit1 == 0:
        return char0
    return common.SERIALIZE_POS1_TABLE[digit1] + char0


def serialize_list(values_list):
    return ''.join(map(lambda value: serialize_value(value), values_list))


def serialize_text(text):
    values_list = parse_text(text)
    return serialize_list(values_list)


def parse_text(text):
    values_list = []
    
    trimmed_text = text.strip()
    splitted_text = trimmed_text.split(common.SERIALIZE_ITEM_DELIMETER)

    def raise_error(msg):
        raise common.ParseError(msg)

    for curr_str in splitted_text:
        if len(curr_str) == 0:
            continue

        if not common.is_numeric(curr_str):
            raise_error('Text contains non numeric item(%s)' % curr_str)

        value = int(curr_str)
        if value < common.MIN_NUMBER or \
           value > common.MAX_NUMBER:
            raise_error('Value is out of range(%i)' % value)

        if len(values_list) == common.MAX_LIST_LENGTH:
            raise_error('Number of values exceeds size limit(%i)' % common.MAX_LIST_LENGTH)

        values_list.append(value)

    return values_list


def parse_input():
    if len(sys.argv) == 2:
        return sys.argv[1]
    
    msg = '''Usage:
    'python serialize_numbers.py arg'
        where arg - list of numbers
'''
    print msg
    raise common.CommandLineError()


if __name__ == '__main__':
    txt = parse_input()
    serialize(txt)
