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
              cmap="jet"):
    """
    plot world map

    Parameters
    -----------
    lat : float or list
        latitude
    long : float or list
        longitude

    Returns
    ----------
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
                         cmap=cmap)
