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
              cmap="jet",
              vmin=None,
              vmax=None,
              ):
    """
    plot world map

    Parameters
    -----------
    lat : float or list
        latitude
    long : float or list
        longitude
    data : float or list
        data (default : None)
    resolutin : str
        cartpy parameter (default : 10m)
    dlon : int or float
        interval of longitude
    dlat : int or float
        interval of latitude
    min_long : int or float
        minimun longitude
    min_lat : int or float
        minimun latitude
    max_long : int or float
        max longitude
    max_lat : int or float
        max latitude
    msize : int
        marker size
    cmap : str
        colormap variation
    vmin : int or float
        min colorbar
    vmax : int or float
        max colorbar

    Returns
    ----------
    fig :matplotlib.Figure
        figure object for plotting
    ax :matplotlib.Axes
        axes object for plot
    """
    # whether int or not
    if type(lat) is int:
        lat = float(lat)
    if type(long) is int:
        long = float(long)
    if type(data) is int:
        data = float(data)

    # whether float or not
    if type(lat) is float:
        llat = []
        llat.append(lat)
    elif type(lat) is list:
        llat = lat

    if type(long) is float:
        llong = []
        llong.append(long)
    elif type(long) is list:
        llong = long

    if vmin is None:
        vmin = min(data)
    if vmax is None:
        vmax = max(data)

    if data is not None:
        if type(data) is float:
            ldat = []
            ldat.append(data)
        elif type(data) is list:
            ldat = data

    fig = plt.figure(figsize=(13,8))
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    ax.coastlines(resolution=resolution)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    if data is not None:
        for inx in range(len(llong)):
            scat = ax.scatter(llong[inx],
                              llat[inx],
                              c=ldat[inx],
                              marker="o",
                              cmap=cmap,
                              vmin=vmin,
                              vmax=vmax)
        fig.colorbar(scat,ax=ax,extend="both")
    else:
        for lon,lat in zip(llong,llat):
            scat = ax.scatter(lon,
                              lat,
                              marker="o",
                              vmin=vmin,
                              vmax=vmax)

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
