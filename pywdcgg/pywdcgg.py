import pandas as pd

class read_file():
    def __init__(self,file):
        """
        Parameters
        ----------
        file : str
            file path and your file name
        """
        self.file = file

    def get_value(self):
        """
        read data from text file that download from WDCGG.

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
        header_list[-1] = header_list[-1][:-1]
        df = pd.read_csv(self.file, skiprows=skiprows, header=None, sep=" ")
        df.columns = header_list

        return df

    def about_info(self):
        """
        get about file info

        Target Information
        ----------
        - site_name
        - latitude
        - longitude
        - elevation
        - parameter
        - start_date
        - end_date
        - units

        Returns
        ----------
        header_info : dict
            header infomation
        """
        header_info = {}

        with open(self.file) as f:
            l_strip = f.readlines()

        skiprows = int(l_strip[0].split(" ")[3]) - 1

        for indx,l in enumerate(l_strip):
            # site_name
            try :
                if l.split(" ")[1] == "site_name":
                    header_info["site_name"] = l.split(":")[1][:-1]
            except IndexError:
                pass

            # parameter
            try :
                if l.split(" ")[1] == "dataset_parameter":
                    header_info["parameter"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # lat
            try :
                if l.split(" ")[1] == "site_latitude":
                    header_info["latitude"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # lon
            try :
                if l.split(" ")[1] == "site_longitude":
                    header_info["longitude"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # elevation
            try :
                if l.split(" ")[1] == "site_elevation":
                    header_info["elevation"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # start_date
            try :
                if l.split(" ")[1] == "dataset_start_date":
                    header_info["start_date"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # end_date
            try :
                if l.split(" ")[1] == "dataset_end_date":
                    header_info["end_date"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass

            # units
            try :
                if l.split(" ")[1] == "value_unc:units":
                    header_info["unit"] = l.split(" ")[-1][:-1]
            except IndexError:
                pass
            if indx == skiprows:
                break

        return header_info

# linear interpolation about lat,lon,height
