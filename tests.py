import unittest
import logging
import common
import generate_numbers as gennum
import serialize_numbers as sernum
import deserialize_numbers as desnum


class TestSerialization(unittest.TestCase):
    def check_serialization(self, numbers):
        in_text = gennum.numbers_to_string(numbers)            
        serialized_text = sernum.serialize_text(in_text)
        deserialized_text = desnum.deserialize_text(serialized_text)
        self.assertEqual(in_text, deserialized_text)


    def check_random_numbers_serialization(self, size):
        #logging.info('---Test %s random numbers serialization---' % size)
        numbers = gennum.generate_random_numbers(size)
        
        self.check_serialization(numbers)        

    
    def test_00_simple_random_number(self):
        for i in range(0, 10):
            numbers = gennum.generate_random_numbers(1)
            self.check_serialization(numbers)


    def test_10_all_numbers_of_digits1(self):
        numbers = gennum.generate_all_numbers_of_digits1()
        self.check_serialization(numbers)


    def test_11_all_numbers_of_digits2(self):
        numbers = gennum.generate_all_numbers_of_digits2()
        self.check_serialization(numbers)


    def test_12_all_numbers_of_digits3(self):
        numbers = gennum.generate_all_numbers_of_digits3()
        self.check_serialization(numbers)


    def test_20_random_numbers50(self):
        self.check_random_numbers_serialization(50)


    def test_21_random_numbers100(self):
        self.check_random_numbers_serialization(100)


    def test_22_random_numbers500(self):
        self.check_random_numbers_serialization(500)


    def test_23_random_numbers1000(self):
        self.check_random_numbers_serialization(1000)


    def test_30_triple_numbers(self):
        numbers = gennum.generate_random_numbers(300)
        numbers = gennum.duplicate_numbers(numbers, 3)
        self.check_serialization(numbers)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
