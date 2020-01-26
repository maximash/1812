# this function creates a matrix of pixels given the coordinates
# the result is stored in a pandas frame
# then pickled
# to be used as a digital elevation model (DEM)

import srtm
from pyproj import Geod
import pandas as pd
import pickle

centerlon = 29.0 # lower left corner longitude, decimal degrees
centerlat = 47 # lower left corner latitude, decimal degrees
pixels = 100 # size of the pixels, meters
width = 500 # km, size of the DEM
length = 500 #km, size of the DEM
g = Geod(ellps='WGS84') # Use Clarke WGS84 ellipsoid
total_pixels = (width * 1000 / pixels) * (length * 1000 / pixels)

endlon1, urcrnrlat, backaz = g.fwd(centerlon, centerlat, 0, width / 2)
urcrnrlon, endlat2, backaz = g.fwd(centerlon, centerlat, 90, width / 2)
endlon3, llcrnrlat, backaz = g.fwd(centerlon, centerlat, 180, width / 2)
llcrnrlon, endlat4, backaz = g.fwd(centerlon, centerlat, 270, width / 2)

pixel_id = list(range((width * 1000 / pixels)))
intermediate_pixels = width*1000 / pixels - 2

lonlats = []
elevations = []
lonlats.append((llcrnrlon,llcrnrlat))
lonlats += g.npts(llcrnrlon,llcrnrlat,urcrnrlon,llcrnrlat,intermediate_pixels)
lonlats.append((urcrnrlon,llcrnrlat))
el = srtm.get_data()
for i in range (len(lonlats)):
    elevation = el.get_elevation(lonlats[i][1], lonlats[i][0])
    elevations.append(elevation)
data = {'id': pixel_id, 'coordinates': lonlats, 'elevation': elevations}
df = pd.DataFrame(data,columns=['id',  'coordinates', 'elevation'])
pickle.dump(df,  open( "DEM.pickle", "wb" ))
print(df.ix[1, 'elevation'])

#print (total_pixels)
print len((lonlats))
#print len(pixel_id)
#el = srtm.get_data()
#elevation = el.get_elevation(latitude,longitude)









