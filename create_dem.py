# this function creates a matrix of pixels given the coordinates
# the result is stored in a pandas frame
# then pickled
# to be used as a digital elevation model (DEM)

import srtm
from pyproj import Geod

llcrnrlon = 27 # lower left corner longitude, decimal degrees
llcrnrlat = 45 # lower left corner latitude, decimal degrees
urcrnrlon = 30 # upper right corner longitude, decimal degrees
urcrnrlat = 48 # upper right corner latitude, decimal degrees
pixel = 100 # size of the pixels, meters

g = Geod(ellps='WGS84') # Use Clarke WGS84 ellipsoid
az12, az21, width = g.inv(llcrnrlon,llcrnrlat,urcrnrlon,llcrnrlat) # X axis of the map
az12, az21, length = g.inv(llcrnrlon,llcrnrlat,llcrnrlon,urcrnrlat) # X axis of the map

print (width /1000)
print (length/ 1000)
#el = srtm.get_data()
#elevation = el.get_elevation(latitude,longitude)

