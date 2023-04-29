import unittest
import logging
import generate_numbers as gennum
import serialize_numbers as sernum
import deserialize_numbers as desnum

SummaryInTextLength = None
SummarySerializedTextLength = None


def calculate_ratio(text_in_length, text_out_length):
    return (100.0 * text_out_length) / text_in_length


def setUpModule():
    global SummaryInTextLength, \
           SummarySerializedTextLength
    
    SummaryInTextLength = 0
    SummarySerializedTextLength = 0


def tearDownModule():
    average_ratio = calculate_ratio(SummaryInTextLength,
                                    SummarySerializedTextLength)
    logging.info("\n---SUMMARY RESULT---")
    logging.info(" average ratio: ({out_len}/{in_len})={ratio:.1f}%".format(
        out_len=SummarySerializedTextLength,
        in_len=SummaryInTextLength,
        ratio=average_ratio))


class TestSerialization(unittest.TestCase):        
    def check_serialization(self, numbers):
        global SummaryInTextLength, \
               SummarySerializedTextLength
        
        in_text = gennum.numbers_to_string(numbers)            
        serialized_text = sernum.serialize_text(in_text)
        deserialized_text = desnum.deserialize_text(serialized_text)
        self.assertEqual(in_text, deserialized_text)
        in_text_length = len(in_text)
        serialized_text_length = len(serialized_text)
        
        SummaryInTextLength += in_text_length
        SummarySerializedTextLength += serialized_text_length
        
        ratio = calculate_ratio(in_text_length, serialized_text_length)
        logging.info(" ratio: ({out_len}/{in_len})={ratio:.1f}%".format(
            out_len=serialized_text_length,
            in_len=in_text_length,
            ratio=ratio))


    def check_random_numbers_serialization(self, size):
        numbers = gennum.generate_random_numbers(size)        
        self.check_serialization(numbers)        

    
    def test_00_simple_random_number(self):
        for i in range(0, 10):
            logging.info('\nTest single number')
            numbers = gennum.generate_random_numbers(1)
            self.check_serialization(numbers)


    def test_10_all_numbers_of_digits1(self):
        logging.info('\nTest all numbers of 1 digit')
        numbers = gennum.generate_all_numbers_of_digits1()
        self.check_serialization(numbers)


    def test_11_all_numbers_of_digits2(self):
        logging.info('\nTest all numbers of 2 digits')
        numbers = gennum.generate_all_numbers_of_digits2()
        self.check_serialization(numbers)


    def test_12_all_numbers_of_digits3(self):
        logging.info('\nTest all numbers of 3 digits')
        numbers = gennum.generate_all_numbers_of_digits3()
        self.check_serialization(numbers)


    def test_20_random_numbers50(self):
        logging.info('\nTest 50 random numbers')
        self.check_random_numbers_serialization(50)


    def test_21_random_numbers100(self):
        logging.info('\nTest 100 random numbers')
        self.check_random_numbers_serialization(100)


    def test_22_random_numbers500(self):
        logging.info('\nTest 500 random numbers')
        self.check_random_numbers_serialization(500)


    def test_23_random_numbers1000(self):
        logging.info('\nTest 1000 random numbers')
        self.check_random_numbers_serialization(1000)


    def test_30_triple_numbers(self):
        logging.info('\nTest 300 tripple numbers')                     
        numbers = gennum.generate_random_numbers(300)
        numbers = gennum.duplicate_numbers(numbers, 3)
        self.check_serialization(numbers)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(message)s")
    unittest.main()
