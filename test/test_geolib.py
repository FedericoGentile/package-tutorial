import os
import sys
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/geolib')))

import unittest
from src.geolib.geolib import distance

class DistanceCalculationTests(unittest.TestCase):
    def test_distance_deg_to_km(self):
        result = distance(40, -80, 35, -120, Deg_Rad='Deg', Km_Ft_NM='Km')
        self.assertAlmostEqual(result, 3542.1, places=1)

    def test_distance_deg_to_ft(self):
        result = distance(40, -80, 35, -120, Deg_Rad='Deg', Km_Ft_NM='Ft')
        self.assertAlmostEqual(result, 11621129.6, places=1)

    def test_distance_deg_to_nm(self):
        result = distance(40, -80, 35, -120, Deg_Rad='Deg', Km_Ft_NM='NM')
        self.assertAlmostEqual(result, 1912.6, places=1)

    def test_distance_rad_to_km(self):
        result = distance(0.6981317007977318, -1.3962634015954636, 0.6108652381980153, -2.0943951023931957, Deg_Rad='Rad', Km_Ft_NM='Km')
        self.assertAlmostEqual(result, 3542.1, places=1)

    def test_distance_rad_to_ft(self):
        result = distance(0.6981317007977318, -1.3962634015954636, 0.6108652381980153, -2.0943951023931957, Deg_Rad='Rad', Km_Ft_NM='Ft')
        self.assertAlmostEqual(result, 11621129.6, places=1)

    def test_distance_rad_to_nm(self):
        result = distance(0.6981317007977318, -1.3962634015954636, 0.6108652381980153, -2.0943951023931957, Deg_Rad='Rad', Km_Ft_NM='NM')
        self.assertAlmostEqual(result, 1912.6, places=1)

if __name__ == '__main__':
    unittest.main()