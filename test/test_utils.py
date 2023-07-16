# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/geolib')))

from src.geolib.utils.utils import (
    convert_coordinates,
    convert_distance
)
import unittest


class CoordinateConversionTests(unittest.TestCase):
    def test_convert_coordinates_deg_to_rad(self):
        lat_a, lon_a, lat_b, lon_b = convert_coordinates(40, -80, 35, -120, Deg_Rad='Deg')
        self.assertAlmostEqual(lat_a, 0.6981317007977318)
        self.assertAlmostEqual(lon_a, -1.3962634015954636)
        self.assertAlmostEqual(lat_b, 0.6108652381980153)
        self.assertAlmostEqual(lon_b, -2.0943951023931957)

    def test_convert_coordinates_rad_to_rad(self):
        lat_a, lon_a, lat_b, lon_b = convert_coordinates(0.6981317007977318, -1.3962634015954636, 0.6108652381980153, -2.0943951023931957, Deg_Rad='Rad')
        self.assertAlmostEqual(lat_a, 0.6981317007977318)
        self.assertAlmostEqual(lon_a, -1.3962634015954636)
        self.assertAlmostEqual(lat_b, 0.6108652381980153)
        self.assertAlmostEqual(lon_b, -2.0943951023931957)

    def test_convert_coordinates_invalid_unit(self):
        with self.assertRaises(Exception):
            convert_coordinates(40, -80, 35, -120, Deg_Rad='InvalidUnit')


class DistanceConversionTests(unittest.TestCase):
    def test_convert_distance_km_to_ft(self):
        result = convert_distance(10, Km_Ft_NM='Ft')
        self.assertAlmostEqual(result, 32808.4)

    def test_convert_distance_km_to_nm(self):
        result = convert_distance(10, Km_Ft_NM='NM')
        self.assertAlmostEqual(result, 5.39957)

    def test_convert_distance_km_to_km(self):
        result = convert_distance(10, Km_Ft_NM='Km')
        self.assertAlmostEqual(result, 10)

    def test_convert_distance_invalid_unit(self):
        with self.assertRaises(Exception):
            convert_distance(10, Km_Ft_NM='InvalidUnit')


if __name__ == '__main__':
    unittest.main()
