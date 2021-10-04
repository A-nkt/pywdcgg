import pwcalc as pwc

# linear interpolation about lat,lon,height
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
