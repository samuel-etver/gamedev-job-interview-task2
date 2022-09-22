import common
import sys


def deserialize(text):
    numbers_list = deserialize_text_to_list(text)
    print(format_deserialized(numbers_list))


def deserialize_text(text):
    numbers_list = deserialize_text_to_list(text)
    return format_deserialized(numbers_list)
    

def deserialize_text_to_list(text):
    out_list = []

    text = text.strip()

    parse_data = {'char_index': 0}

    def get_char():
        if not has_char():
            return None
        char_index = parse_data['char_index']
        char = text[char_index]
        parse_data['char_index'] = char_index + 1
        return char

    def has_char():
        return parse_data['char_index'] < len(text)    

    table0 = common.DESERIALIZE_POS0_TABLE
    table1 = common.DESERIALIZE_POS1_TABLE

    def is_char_of_pos0(char):
        return table0.has_key(char)

    def is_char_of_pos1(char):
        return table1.has_key(char)
        
    def deserialize_one_char(char):
        return table0[char]
    
    def deserialize_two_chars(first_char, second_char): 
        return table0[second_char] + table1[first_char]*common.SERIALIZE_POS0_TABLE_SIZE

    def deserialize_chars(first_char, second_char):
        if second_char == None:
            return deserialize_one_char(first_char)
        return deserialize_two_chars(first_char, second_char)

    def raise_error(msg):
        raise common.ParseError(msg)
    

    while has_char():
        first_char = get_char()
        second_char = None

        if is_char_of_pos1(first_char):
            if not has_char():
                pass
            second_char = get_char()
            if not is_char_of_pos0(second_char):
                raise_error('Unexpected char(%s)' % second_char)
        elif not is_char_of_pos0(first_char):
            raise_error('Unexpected char(%s)' % first_char)
            
        value = deserialize_chars(first_char, second_char)
        out_list.append(value)
    
    return out_list


def format_deserialized(numbers_list):
    str_list = map(str, numbers_list)
    return ' '.join(str_list)


def parse_input():
    if len(sys.argv) == 2:
        return sys.argv[1]
    
    msg = '''Usage:
    'python deserialize_numbers.py arg'
        where arg - string
'''
    print msg
    raise common.CommandLineError()


if __name__ == '__main__':
    text = parse_input()
    deserialize(text)
