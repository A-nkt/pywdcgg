import sys
sys.path.append("../../pywdcgg/")
import pywdcgg as pw

# test data
# hfc134a : ../data/hfc134a/MHD/monthly/hfc134a_mhd_surface-insitu_4_2023-2022_monthly.txt
# ch4 : ../data/ch4/SYO/monthly/ch4_syo_surface-flask_2_3001-9999_monthly.txt
# ch4 : ../data/ch4/SYO/event/ch4_syo_surface-flask_2_3001-9999_event.txt
rdat = pw.read_file("../data/ch4/SYO/monthly/ch4_syo_surface-flask_2_3001-9999_monthly.txt")

dat = rdat.get_value()
