import sys
sys.path.append("../../pywdcgg/")
import pywdcgg as pw
import matplotlib.pyplot as plt
import random

dat = [];lon = [];lat = []
for _ in range(100):
    dat.append(random.randint(0,100))
    lon.append(random.randint(-180,180))
    lat.append(random.randint(-90,90))
fig,ax = pw.world_map(lon,lat,data=dat,cmap="RdBu")
#fig,ax = pw.world_map(36.5,
#                      137.5,
#                      max_long=150,
#                      min_long=100,
#                      max_lat=60,
#                      min_lat=20,
#                      dlon=10,
#                      dlat=10)
plt.show()
