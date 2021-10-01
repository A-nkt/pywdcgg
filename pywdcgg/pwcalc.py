"""
In this file, mainly using calculation program.
"""
import pandas as pd

class Get_Value():
    """
    make datafile and organized data
    """
    def __init__(self,file):
        with open(file) as f:
            l_strip = f.readlines()
        # molding file
        skiprows = int(l_strip[0].split(" ")[3])
        header_list = l_strip[skiprows-1].split(" ")[1:]
        header_list[-1] = header_list[-1][:-1]
        self.df = pd.read_csv(file, skiprows=skiprows, header=None, sep=" ")
        self.df.columns = header_list

    def to_dataframe(self):
        return self.df

    def make_date(self):
        """
        make date column YYYYY/MM

        Parameters
        ----------
        self.df : pd.DataFrame
            input dataframe

        Returns
        ----------
        self.df : pd.DataFrame
            output dataframe
        """
        #try :
        #    for ix in range(len(self.df)):
        #        print(self.df.loc[ix,"year"],self.df.loc[ix,"month"])
        #        self.df.loc[ix,"date"] = "{}/{}".format(self.df.loc[ix,"year"],self.df.loc[ix,"month"])
        #except KeyError:
        #    return "Can't find year or month column"
        return "Hello World"

# import file and organize
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
        return Get_Value(self.file)

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
