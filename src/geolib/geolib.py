import numpy as np
from .utils import convert_coordinates, convert_distance

R = 6371 # km

def distance(lat_a, lon_a, lat_b, lon_b, Deg_Rad = 'Deg', Km_Ft_NM = 'Km'):
    """
    Calculate the distance between two coordinates using the Haversine formula.

    Args:
        lat_a (float): Latitude of point A.
        lon_a (float): Longitude of point A.
        lat_b (float): Latitude of point B.
        lon_b (float): Longitude of point B.
        Deg_Rad (str, optional): Unit of latitude and longitude inputs. Can be either 'Deg' for degrees or 'Rad' for radians. Defaults to 'Deg'.
        Km_Ft_NM (str, optional): Unit of distance output. Can be either 'Km' for kilometers, 'Ft' for feet, or 'NM' for nautical miles. Defaults to 'Km'.

    Returns:
        float: The calculated distance between the two coordinates.

    """
    # Covert coordinates to desired unit
    lat_a, lon_a, lat_b, lon_b = convert_coordinates(lat_a, lon_a, lat_b, lon_b, Deg_Rad)
    
    # Haversine formula returns great circle [Km]
    a = np.sin((lat_b-lat_a)/2)**2 + np.cos(lat_a)*np.cos(lat_b)*np.sin(((lon_b-lon_a)/2))**2
    c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = R*c
    
    # Convert to distance to the desired unit
    d = convert_distance(d, Km_Ft_NM)
    
    return d