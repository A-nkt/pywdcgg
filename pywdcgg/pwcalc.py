import pandas as pd
"""
In this file, mainly using calculation program.
"""
class Get_Value(object):
    """
    make datafile and organized data
    """
    def __init__(self,file):
        """
        read data from text file that download from WDCGG.

        Returns
        ----------
        df : pd.DataFrame
            output file
        """
        with open(file) as f:
            l_strip = f.readlines()
        # molding file
        skiprows = int(l_strip[0].split(" ")[3])
        header_list = l_strip[skiprows-1].split(" ")[1:]
        header_list[-1] = header_list[-1][:-1]
        self.df = pd.read_csv(file, skiprows=skiprows, header=None, sep=" ")
        ndate = ["year", "month", "day", "hour", "minute", "minute"]
        for iax,colname in enumerate(header_list):
            if iax >= 7 and iax <= 12:
                if colname in ndate:
                    header_list[iax] = header_list[iax] + "_2"
        self.df.columns = header_list
        self.df = self.df.drop(["year_2", "month_2", "day_2", "hour_2", "minute_2", "minute_2"], axis=1)

    def to_rowDataFrame(self):
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
        try :
            header_list = self.df.columns
            for ix in range(len(self.df)):
                self.df.loc[ix,"date"] = "{}/{}".format(self.df.loc[ix,"year"],str(self.df.loc[ix,"month"]).zfill(2))
            header_list = header_list.insert(0, "date")
            self.df = self.df[header_list]
        except KeyError:
            return "Can't find year or month column"
        return self.df


# import file and organize
class read_file(Get_Value):
    def __init__(self,file):
        """
        Parameters
        ----------
        file : str
            file path and your file name
        """
        self.file = file
        super().__init__(self.file) #read_file(class)で定義したクラスの__init__メソッドをインスタンス化

    def get_value(self,make_date=False,syr=None,fyr=None):
        """
        read data from text file that download from WDCGG.

        Parameters
        ----------
        make_date : bool
            if YYYY/MM add or not
        """
        if make_date:
            dx = super().make_date()
        else:
            dx = super().to_rowDataFrame()

        if syr is not None:
            dx = dx[dx["year"] >= syr]
        if fyr is not None:
            dx = dx[dx["year"] <= fyr]

        dx = dx.reset_index(drop=True)
        return dx

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
