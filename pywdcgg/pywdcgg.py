import pwcalc as pwc
import pwplot as pwt

def read_file(file):
    """
    read_file class

    Parameters
    -----------
    file : str
        file that you want

    Returns
    -----------
    pwx.reaad_file : read_file class instansce

    """
    return pwc.read_file(file)

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
    return pwt.world_map(lat,
                         long,
                         data=data,
                         resolution=resolution,
                         dlon=dlon,
                         dlat=dlat,
                         min_long=min_long,
                         min_lat=min_lat,
                         max_long=max_long,
                         max_lat=max_lat,
                         msize=msize,
                         cmap=cmap,
                         vmin=vmin,
                         vmax=vmax,
                         )
