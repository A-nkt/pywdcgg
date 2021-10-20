import sys
sys.path.append("../../pywdcgg/")
import pywdcgg as pw
import matplotlib.pyplot as plt
import random

lon = 136.6
lat = 36.6
data = 10

fig,ax = pw.world_map(lon,lat,data=data)
#fig,ax = pw.world_map(36.5,
#                      137.5,
#                      max_long=150,
#                      min_long=100,
#                      max_lat=60,
#                      min_lat=20,
#                      dlon=10,
#                      dlat=10)
plt.show()
