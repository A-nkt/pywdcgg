import pandas as pd

class read_file():
    def __init__(self,file):
        self.file = file

    def get_value(self):
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
        # read data from txt file
        with open(self.file) as f:
            l_strip = f.readlines()
        # molding file
        skiprows = int(l_strip[0].split(" ")[3])
        header_list = l_strip[skiprows-1].split(" ")[1:]
        df = pd.read_csv(self.file, skiprows=skiprows, header=None, sep=" ")
        df.columns = header_list

        return df

    def about_info(self):
        """
        get about file info
        """
        pass


# linear interpolation about lat,lon,height
