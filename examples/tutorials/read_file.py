import sys
sys.path.append("../../pywdcgg/")
import pywdcgg as pw

ch4 = pw.read_file("../data/CH4/SYO/monthly/ch4_syo_surface-flask_2_3001-9999_monthly.txt")
ch4 = ch4.get_value()
