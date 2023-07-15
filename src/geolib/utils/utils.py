import numpy as np

def convert_coordinates(lat_a, lon_a, lat_b, lon_b, Deg_Rad):
    """
    Convert latitude and longitude coordinates from degrees to radians (or vice versa).

    Args:
        lat_a (float): Latitude of point A.
        lon_a (float): Longitude of point A.
        lat_b (float): Latitude of point B.
        lon_b (float): Longitude of point B.
        Deg_Rad (str): Unit of input coordinates. Valid values are 'Deg' for degrees
            and 'Rad' for radians.

    Returns:
        tuple: A tuple containing the converted latitude and longitude coordinates of point A
            and point B in the specified units.

    Raises:
        Exception: If Deg_Rad is not 'Deg' or 'Rad'.

    Example:
        >>> convert_coordinates(40, -80, 35, -120, Deg_Rad='Deg')
        (0.6981317007977318, -1.3962634015954636, 0.6108652381980153, -2.0943951023931957)
    """
    if Deg_Rad == 'Deg':
        lat_a, lon_a, lat_b, lon_b = np.deg2rad(lat_a), np.deg2rad(lon_a), np.deg2rad(lat_b), np.deg2rad(lon_b)
    elif Deg_Rad == 'Rad':
        pass
    else:
        raise Exception("Deg_Rad must be either 'Deg' or 'Rad'.")
        
    return lat_a, lon_a, lat_b, lon_b
    
def convert_distance(d, Km_Ft_NM):
    """
    Convert a distance value from kilometers to feet or nautical miles.

    Args:
        d (float): The distance value to be converted.
        Km_Ft_NM (str): Unit of input distance. Valid values are 'Km' for kilometers,
            'Ft' for feet and 'NM' for Nautical Miles.

    Returns:
        float: The converted distance value.

    Raises:
        Exception: If Km_Ft_NM is not set to either 'Km', 'Ft', or 'NM'.
    """    
    if Km_Ft_NM == 'Ft':
        d = d*3280.84
    elif Km_Ft_NM == 'NM':
        d = d*0.539957
    elif Km_Ft_NM == 'Km':
        pass
    else:
        raise Exception("Km_Ft_NM must be either 'Km', 'Ft' or 'NM'.")
        
    return d