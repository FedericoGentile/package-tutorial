# Geolib
Package to calculate distances between 2 points on the Earth.

## Installation
Use the package manager pip to install package-name.
```sh
pip install geolib
```

## Usage
Calculate the distance between 2 geographical coordinates:
```py
from geolib import distance

result = distance(40, -80, 35, -120, Deg_Rad='Deg', Km_Ft_NM='NM')
```

Expected result: **1912.2 NM**.

## Developing
To install geolib, along with the tools you need to develop and run tests, run the 
following in your virtual environment:
```sh
pip install geolib[dev]
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
federico@gentile.com