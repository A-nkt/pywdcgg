import pandas as pd

class read_file():
    def __init__(self,dir_file):
        """
        read data from text file that download from WDCGG.

        Parameters
        ----------
        dir_file : str
            file path and your file name

        Returns
        ----------
        df : pd.DataFrame
            output file

        """
        with open(dir_file) as f:
            data_get = False
            l_strip = [s.strip() for s in f.readlines()]
            for indx,l in enumerate(l_strip):
                if l[0] != "#":
                    header_row = l_strip[indx-1]
                    skiprows = indx
                    break

        header_list = header_row.split(" ")[1:]
        df = pd.read_csv(dir_file,skiprows=skiprows,header=None,sep=" ")
        df.columns = header_list
        print(df)
    def Info(self):
        """
        get about file info
        """
        pass


# linear interpolation about lat,lon,height
