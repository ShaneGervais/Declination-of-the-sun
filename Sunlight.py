"""
While the stars in our solar systems stays at a constant
declination, our sun doesn't due to the tilt of the earths
equatorial axis throughout the year. Resulting in winter
solstice having longer night and the summer solstice having
longer days.
"""

import math
import numpy as np
from astropy.coordinates import EarthLocation
import astropy.units as u
import matplotlib.pyplot as plt

#geograhical position of the observer
observer = EarthLocation(lat=53*u.deg+28*u.arcmin+49*u.arcsec, lon=10*u.deg+14*u.arcmin+23*u.arcsec)

N = np.arange(365) #number of days in a year
omega = 2*math.pi/365.24 #angular velocity
epsilon = math.radians(23.44) #obliquity of ecliptic

#declination of the sun
delta = -np.arcsin(np.sin(epsilon) * np.cos(omega*(N+10)))

#Different locations on earth (latitudes included)
loc = {
    'Hamburg'       : observer.lat.radian,
    'Fredericton'   : math.radians(45.9636),
    'Moncton'       : math.radians(46.0532),
    'Saint John'    : math.radians(45.1513),
    'Raglan Mine'   : math.radians(61.6872),
    'Rio de Janero' : math.radians(22.9068),
    'Sydney'        : math.radians(33.8688),
    'Paris'         : math.radians(48.8566),
    'Bangkok'       : math.radians(13.7563),
    'London'        : math.radians(51.5072)
    }


for i in loc:
    #print latitude in term for each location
    print(i + ": {:.2f} deg".format(math.degrees(loc[i])))

    #calculate day lenght in solar hours
    h = np.arccos(np.clip(-np.tan(delta) * math.tan(loc[i]), -1.0, 1.0))
    T = (np.degrees(2*h)/360)*u.sday.to(u.h)

    #plot results
    plt.plot(N, T, label=i)

#labels
plt.xlabel("Days")
plt.ylabel("Length of day (/h)")
#axis limits
plt.xlim(0,364)
plt.ylim(0,24)
plt.legend(loc='upper right')
plt.show()