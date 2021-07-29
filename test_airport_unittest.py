import unittest
from airport import Airport

class TestAirport(unittest.TestCase):

    # https://docs.python.org/3/library/unittest.mock.html
    # from unittest.mock import MagicMock
    # thing = ProductionClass()
    # thing.method = MagicMock(return_value=3)
    
    def test_airport_land(self):
        test_airport = Airport()
        test_airport.land("test_plane")
        test_airport.land("2")
        actual = test_airport.view_hangar()
        expected = ['test_plane', '2']
        self.assertEqual(len(actual), 2)
        self.assertEqual(expected, actual)

    def test_airport_plane_take_off(self):
        test_airport = Airport()
        test_airport.land("grounded_plane")
        test_airport.land("leaving_plane")
        test_airport.take_off("leaving_plane")
        actual = test_airport.view_hangar()
        expected = "leaving_plane"
        self.assertNotIn(expected, actual)

    def test_airport_capacity(self):
        test_airport = Airport()
        for i in range(4):
            test_airport.land("grounded_plane")
        self.assertRaises(Exception, test_airport.land("grounded_plane"))



if __name__ == '__main__':
    unittest.main()