from unittest import TestCase
from AOC_day_05 import intcode


class TestIntcode(TestCase):
    
    def test_intcode_01(self):
        input_state = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=3)[1], 0)
    
    def test_intcode_02(self):
        input_state = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=8)[1], 1)
    
    def test_intcode_03(self):
        input_state = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=9)[1], 0)
    
    def test_intcode_04(self):
        input_state = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=3)[1], 1)
    
    def test_intcode_05(self):
        input_state = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=8)[1], 0)
    
    def test_intcode_06(self):
        input_state = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(intcode(input_state, input_init=9)[1], 0)
    
    def test_intcode_07(self):
        input_state = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=3)[1], 0)
    
    def test_intcode_08(self):
        input_state = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=8)[1], 1)
    
    def test_intcode_09(self):
        input_state = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=9)[1], 0)
    
    def test_intcode_10(self):
        input_state = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=3)[1], 1)
    
    def test_intcode_11(self):
        input_state = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=8)[1], 0)
    
    def test_intcode_12(self):
        input_state = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(intcode(input_state, input_init=9)[1], 0)
    
    def test_intcode_13(self):
        input_state = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(intcode(input_state, input_init=0)[1], 0)
    
    def test_intcode_14(self):
        input_state = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(intcode(input_state, input_init=5)[1], 1)
    
    def test_intcode_15(self):
        input_state = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(intcode(input_state, input_init=0)[1], 0)
    
    def test_intcode_16(self):
        input_state = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(intcode(input_state, input_init=5)[1], 1)
    
    def test_intcode_17(self):
        input_state = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                       1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
                       4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1,
                       20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(intcode(input_state, input_init=3)[1], 999)
    
    def test_intcode_18(self):
        input_state = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                       1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
                       4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1,
                       20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(intcode(input_state, input_init=8)[1], 1000)
    
    def test_intcode_19(self):
        input_state = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20,
                       1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
                       4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1,
                       20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(intcode(input_state, input_init=9)[1], 1001)
