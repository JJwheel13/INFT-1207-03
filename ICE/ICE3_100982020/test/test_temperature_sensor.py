import unittest
from src.temperature_sensor import process_temperatures

class TestTemperatureSensor(unittest.TestCase):
    def test_minimum_boundary(self):
        self.assertEqual(process_temperatures(["-50", "0", "0"]), "Min: -50°C, Max: 0°C, Avg: -16.67°C")

    def test_maximum_boundary(self):
        self.assertEqual(process_temperatures(["150", "0", "0"]), "Min: 0°C, Max: 150°C, Avg: 50°C")

    def test_nearby_boundaries(self):
        self.assertEqual(process_temperatures(["-49.9", "149.9", "0"]), "Min: -49.9°C, Max: 149.9°C, Avg: 33.33°C")

    def test_valid_invalid_inputs(self):
        self.assertEqual(process_temperatures(["-60", "20", "160"]), "Min: 20°C, Max: 20°C, Avg: 20°C")

    def test_alphabetical_input(self):
        self.assertEqual(process_temperatures(["-40", "hello", "60"]), "Min: -40°C, Max: 60°C, Avg: 10°C")

    def test_special_char_input(self):
        self.assertEqual(process_temperatures(["-30", "70", "$"]), "Min: -30°C, Max: 70°C, Avg: 20°C")

    def test_mathematical_input(self):
        self.assertEqual(process_temperatures(["(6*18)-8", "(300/3)-50", "(2*-5)+10"]), "Min: 0°C, Max: 100°C, Avg: 50.0°C")

    def test_invalid_mathematical_input(self):
        self.assertEqual(process_temperatures(["(1/0)"]), "No valid input provided.")

    def test_matching_input(self):
        self.assertEqual(process_temperatures(["1", "1", "1"]), "Min: 1°C, Max: 1°C, Avg: 1°C")

    def test_empty_input(self):
        self.assertEqual(process_temperatures([]), "No valid input provided.")

    def test_invalid_input(self):
        self.assertEqual(process_temperatures(["a", "b", "c"]), "No valid input provided.")

    def test_small_input(self):
        self.assertEqual(process_temperatures(["0.0000000001", "1", "1"]), "Min: 1e-10°C, Max: 1°C, Avg: 0.67°C")

if __name__ == '__main__':
    unittest.main()
