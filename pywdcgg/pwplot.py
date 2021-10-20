import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
"""
In this file, plot about wdcgg data.
"""


def world_map(lat,
              long,
              data=None,
              resolution="10m",
              dlon=60,
              dlat=30,
              min_long=-180,
              min_lat=-90,
              max_long=180,
              max_lat=90,
              msize=30,
              cmap="jet"):
    """
    plot world map
    
    Parameters
    ----------
    lat : float or list 
        latitude
    long : float or list 
        longtitude
    data : float or list
        mapping data
    resolutin : str
        cartpy parameter(defalut : 10m)
    dlon : float
    dlat : float
    min_long : float
    min_lat : float
    max_long : float
    max_lat : float
    msize : float
    
    Returns
    ----------
    """
    if type(lat) is int:
        lat = float(lat)
    if type(long) is int:
        long = float(long)        
    if type(data) is int:
        data = float(data)     
        
    if type(lat) is float:
        llat = []
        llat.append(lat)
    if type(long) is float:
        llong = []
        llong.append(long)
    if data is not None:
        if type(data) is float:
            ldat = []
            ldat.append(data) 
    
    fig = plt.figure(figsize=(13,8))
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    ax.coastlines(resolution=resolution)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    
    if data is not None:
        for inx in range(len(llong)):
            scat = ax.scatter(llong[inx], llat[inx], c=ldat[inx], marker="o", cmap=cmap)
    else:
        for lon,lat in zip(llong,llat):
            scat = ax.scatter(lon, lat, marker="o",cmap=cmap)
            
    fig.colorbar(scat,ax=ax,extend="both")
    xticks_lab = np.arange(-180, 180, dlon)
    yticks_lab = np.arange(-90, 90.01, dlat)
    ax.set_xticks(xticks_lab, crs=ccrs.PlateCarree())
    ax.set_yticks(yticks_lab, crs=ccrs.PlateCarree())
    ax.set_xlabel("Longtitude")
    ax.set_ylabel("Latitude")
    gl = ax.gridlines(crs=ccrs.PlateCarree())
    gl.xlocator = mticker.FixedLocator(np.arange(-180, 180.1, dlon))
    gl.ylocator = mticker.FixedLocator(np.arange(-90, 90.1, dlat)) 
    ax.set_extent([min_long, max_long, min_lat, max_lat])
    return fig,ax