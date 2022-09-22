MAX_NUMBER = 300
MIN_NUMBER = 1
MAX_LIST_LENGTH = 1000
TEST_FOLDER = 'TEST'

SERIALIZE_POS0_TABLE = {}
SERIALIZE_POS1_TABLE = {}
DESERIALIZE_POS0_TABLE = {}
DESERIALIZE_POS1_TABLE = {}

SERIALIZE_POS0_TABLE_SIZE = 0
SERIALIZE_POS1_TABLE_SIZE = 0
SERIALIZE_ITEM_DELIMETER = ' '


class CommandLineError(Exception):
    pass


class ParseError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def create_serialize_pos0_table():    
    chars_list = concat_lists(rangeChars('A', 'Z'),
                              rangeChars('a', 'z'))
    return create_serialize_table(chars_list)


def create_serialize_pos1_table():
    chars_list = rangeChars('0', '9')
    return create_serialize_table(chars_list)


def create_deserialize_pos0_table():
    return create_deserialize_table(SERIALIZE_POS0_TABLE)


def create_deserialize_pos1_table():
    return create_deserialize_table(SERIALIZE_POS1_TABLE)


def create_deserialize_table(serialize_table):
    deserialize_table = {}
    for key in serialize_table:
        value = serialize_table[key]        
        deserialize_table[value] = key
    return deserialize_table


def rangeChars(fromChar, toChar):
    result = []
    for charOrd in xrange(ord(fromChar), ord(toChar) + 1):
        result.append(chr(charOrd))
    return result


def concat_lists(*lists):    
    result = []
    for curr_list in lists:
        for element in curr_list:
            result.append(element)
    return result


def create_serialize_table(chars_list):
    table = {}
    index = 0
    for curr_char in chars_list:
        table[index] = curr_char
        index += 1
    return table

    
def is_numeric(text):
    return text.isdigit()


def init():
    global SERIALIZE_POS0_TABLE, \
           SERIALIZE_POS1_TABLE, \
           DESERIALIZE_POS0_TABLE, \
           DESERIALIZE_POS1_TABLE, \
           SERIALIZE_POS0_TABLE_SIZE, \
           SERIALIZE_POS1_TABLE_SIZE
    
           
    SERIALIZE_POS0_TABLE = create_serialize_pos0_table()
    SERIALIZE_POS1_TABLE = create_serialize_pos1_table()
    DESERIALIZE_POS0_TABLE = create_deserialize_pos0_table()
    DESERIALIZE_POS1_TABLE = create_deserialize_pos1_table()

    SERIALIZE_POS0_TABLE_SIZE = len(SERIALIZE_POS0_TABLE)
    SERIALIZE_POS1_TABLE_SIZE = len(SERIALIZE_POS1_TABLE)


init()
