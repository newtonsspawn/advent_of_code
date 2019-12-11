from unittest import TestCase
from AOC_day_06 import count_orbits


class TestCountOrbits(TestCase):
    def test_count_orbits_01(self):
        with open('./test_input.txt', 'r') as f:
            inputs = f.readlines()
        map_data = [i.strip() for i in inputs]
        self.assertEqual(count_orbits(map_data), 42)
    
    def test_count_orbits_02(self):
        with open('./test_input_y&s.txt', 'r') as f:
            inputs = f.readlines()
        map_data = [i.strip() for i in inputs]
        self.assertEqual(count_orbits(map_data, layout=True), 4)
