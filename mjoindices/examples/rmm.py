import numpy as np
import time
import sys 
sys.path.append("../../site-packages/mjoindices/")

#fish://l.kostin@77.247.240.205/home/l.kostin/.local/lib/python3.10/site-packages/mjoindices/
#data90t/geosci/rrd/slav/olr/2p5/
from scipy.io import netcdf
import netCDF4 as netcdf4
from pathlib import Path

import olr_handling as olr
import mjoindices.u200_handling as u200
import mjoindices.u850_handling as u850
import mjoindices.sst_handling as sst

from data_to_dataframe import *
from preanalysis import *

from eofs.multivariate.standard import MultivariateEof

start_time = time.time()

#TODO path+name, git, make functions universal, dependence on name, cmp7ppc for short olr

#1993-, 2004+, 2006, 2018 '../tests/testdata/1991-2019_2p5grid/Dec.30/'


#-rw-r--r-- 1 l.kostin users 9903664 Dec  8 16:49 erfclim.041230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.041230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.041230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903664 Dec  8 16:49 erfclim.061230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.061230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.061230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903856 Dec  8 16:49 erfclim.181230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.181230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.181230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903856 Dec  8 16:49 erfclim.931230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.931230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.931230.ensmean-u850-anom-2p5grid.nc



#ncfile_olr_path = '../tests/testdata/era5-olr-2p5grid-2015.nc' #N
#ncfile_olr_path = '../tests/testdata/era5-olr-day-anom-2p5grid.nc'
#era5-u850hpa-anom-day-2p5grid-2006.nc
#ncfile_olr_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2006.nc' #norm without sst correction
ncfile_olr_path = '../tests/testdata/era5-olr-day-2p5grid-2015-hp.nc' 
#ncfile_olr_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-radtt-anom-2p5grid.nc' # plav
#ncfile_olr_path = '../tests131230/testdata/plv-olr-anom-day-2p5-2015.nc'

#ncfile_u200_path = '../tests/testdata/era5-u200hpa-2p5grid-2015.nc'
#ncfile_u200_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2006.nc'#norm without sst correction
ncfile_u200_path = '../tests/testdata/era5-u200hpa-day-2p5grid-2015-hp.nc' 
#ncfile_u200_path = '../tests/testdata/erfclim.15123018-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/our-u200hpa-anom-day-2p5-2015-f3lp.nc'

#ncfile_u850_path = '../tests/testdata/era5-u850hpa-2p5grid-2015.nc' # N, NN
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5-2004.nc'#norm without sst correction 
ncfile_u850_path = '../tests/testdata/era5-u850hpa-day-2p5grid-2015-hp.nc' # f3lp hp dt
#ncfile_u850_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u850-anom-2p5grid.nc'# plav
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2006.nc'


#ncfile_olr_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u200_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u850_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'

#not Anomaly
#ncfile_olr_120_path = '../tests/testdata/era5-olr-2p5grid-2014.nc'
#ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-2p5grid-2014.nc'
#ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-2p5grid-2014.nc'

#Works Anomaly
ncfile_olr_120_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2014.nc'
ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2014.nc'
ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2014.nc'

ncfile_sst_path = '../tests/testdata/era5-sst-day-2p5grid.nc'

olr_sst_df_file = 'example_data/dataframes/day_sst_olr.txt'
u200_sst_df_file = 'example_data/dataframes/day_sst_u200.txt'
u850_sst_df_file = 'example_data/dataframes/day_sst_u850.txt'

olr_sst_120_df_file = 'example_data/dataframes/day_sst_olr_120.txt'
u200_sst_120_df_file = 'example_data/dataframes/day_sst_u200_120.txt'
u850_sst_120_df_file = 'example_data/dataframes/day_sst_u850_120.txt'

pctxtfile = 'example_data/PCs2-JFM-2.5_full2_aver2_NOsst_15-HP2.txt'
psctxtfile = 'example_data/PsCs-JFM-2.5_full2_aver2_NOsst_-HP2.txt'

day_start = np.datetime64("2015-01-01")
day_end = day_start + np.timedelta64(89, 'D') #89 JFM

##################   tests   ################
#shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end)
#interpolated_olr = olr.interpolate_spatial_grid_to_original(shorter_olr)
#shorter_sst = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)
#interpolated_sst = sst.interpolate_spatial_grid_to_original(shorter_sst)
#save_sst_olr_to_df(day_start, day_end, interpolated_olr, interpolated_sst, olr_sst_df_file)
#exit()
#############################################

#******  Make DataFile from nc files including 120 days before start *******#S
#day_start_120 = day_start - np.timedelta64(120, 'D')
#day_end_120 = day_start - np.timedelta64(1, 'D')
#shorter_olr_120 = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_120_path, day_start_120, day_end_120, plav=False)
#shorter_u200_120 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_120_path, day_start_120, day_end_120, plav=False)
#shorter_u850_120 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_120_path, day_start_120, day_end_120, plav=False)
#shorter_sst_120 = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start_120, day_end_120)

#interpolated_olr_120 = olr.interpolate_spatial_grid_to_original(shorter_olr_120)
#interpolated_u200_120 = u200.interpolate_spatial_grid_to_original(shorter_u200_120)
#interpolated_u850_120 = u850.interpolate_spatial_grid_to_original(shorter_u850_120)
#interpolated_sst_120 = sst.interpolate_spatial_grid_to_original(shorter_sst_120)

#save_sst_olr_to_df(day_start_120, day_end_120, interpolated_olr_120, interpolated_sst_120, olr_sst_120_df_file)
#save_sst_u200_to_df(day_start_120, day_end_120, interpolated_u200_120, interpolated_sst_120, u200_sst_120_df_file)
#save_sst_u850_to_df(day_start_120, day_end_120, interpolated_u850_120, interpolated_sst_120, u850_sst_120_df_file)

#olr_120_path = save_new_dataframe_120(olr_sst_120_df_file, "olr")
#u200_120_path = save_new_dataframe_120(u200_sst_120_df_file, "u200")
#u850_120_path = save_new_dataframe_120(u850_sst_120_df_file, "u850")
#exit()
#***************************************************************************#

shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end, plav=False) #True
shorter_u200 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_path, day_start, day_end, plav=False)
shorter_u850 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_path, day_start, day_end, plav=False)
shorter_sst = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)

interpolated_olr = olr.interpolate_spatial_grid_to_original(shorter_olr)
interpolated_u200 = u200.interpolate_spatial_grid_to_original(shorter_u200)
interpolated_u850 = u850.interpolate_spatial_grid_to_original(shorter_u850)
interpolated_sst = sst.interpolate_spatial_grid_to_original(shorter_sst)

#******  Make DataFile from nc files  *******#
save_sst_olr_to_df(day_start, day_end, interpolated_olr, interpolated_sst, olr_sst_df_file)
save_sst_u200_to_df(day_start, day_end, interpolated_u200, interpolated_sst, u200_sst_df_file)
save_sst_u850_to_df(day_start, day_end, interpolated_u850, interpolated_sst, u850_sst_df_file)
#*******************************************#
#aver 2, 3
#df_sst_olr = get_new_dataframe(olr_sst_df_file, "olr", olr_120_path)
#df_sst_u200 = get_new_dataframe(u200_sst_df_file, "u200", u200_120_path)
#df_sst_u850 = get_new_dataframe(u850_sst_df_file, "u850", u850_120_path)
#aver 
df_sst_olr = get_new_dataframe(olr_sst_df_file, "olr")
df_sst_u200 = get_new_dataframe(u200_sst_df_file, "u200")
df_sst_u850 = get_new_dataframe(u850_sst_df_file, "u850")

variance_olr = np.std(df_sst_olr)
variance_u200 = np.std(df_sst_u200)
variance_u850 = np.std(df_sst_u850)

#exit()
#******  Get data from new dataFrames  ******#
#df_sst_olr = (pd.read_csv("example_data/dataframes/df_new_arrayed_sst_olr.txt"))["olr"].values
#df_sst_u200 = (pd.read_csv("example_data/dataframes/df_new_arrayed_sst_u200.txt"))["u200"].values
#df_sst_u850 = (pd.read_csv("example_data/dataframes/df_new_arrayed_sst_u850.txt"))["u850"].values

#df_sst_olr1 = np.array(df_sst_olr)
#df_sst_u2001 = np.array(df_sst_u200)
#df_sst_u8501 = np.array(df_sst_u850)
#print(df_sst_olr)
#print("len(shorter_olr.olr) :",len(shorter_olr.olr))
#print(len(df_sst_olr))

#********************************************#
print("variance_olr: ",variance_olr, " variance_u200: ", variance_u200, " variance_u850: ", variance_u850)
#******  Find PC  ******#
solver = MultivariateEof([df_sst_olr/variance_olr, df_sst_u200/variance_u200, df_sst_u850/variance_u850], center=True)
#solver = MultivariateEof([interpolated_olr.olr / variance_olr, interpolated_u200.u200 / variance_u200, interpolated_u850.u850 / variance_u850])
pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1))

pc1, pc2 = [], []
for pc in pcs:
    pc1.append(pc[0])
    pc2.append(pc[1]) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
df = pd.DataFrame({"Date": dates, "PC1": pc1, "PC2": pc2})
df.to_csv(pctxtfile, index=False, float_format="%.5f")

pseudo_pcs = np.squeeze(solver.projectField([df_sst_olr/variance_olr, df_sst_u200/variance_u200, df_sst_u850/variance_u850], eofscaling=1, neofs=2))
psc1, psc2 = [], []
for pc in pseudo_pcs:
    psc1.append(pc[0])
    psc2.append(pc[1]) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
df = pd.DataFrame({"Date": dates, "PC1": psc1, "PC2": psc2})
df.to_csv(psctxtfile, index=False, float_format="%.5f")


exit()
#**********************#

#******  Delete Average  ******#
shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end)
anomaly_olr = olr.get_doys_in_span(shorter_olr, ncfile_olr_path, day_start, day_end)
interpolated_olr = olr.interpolate_spatial_grid_to_original(anomaly_olr)
print("--- %s seconds for one span ---" % (time.time() - start_time))

shorter_u200 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_path, day_start, day_end)
anomaly_u200 = u200.get_doys_in_span(shorter_u200, ncfile_u200_path, day_start, day_end)
interpolated_u200 = u200.interpolate_spatial_grid_to_original(anomaly_u200)

shorter_u850 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_path, day_start, day_end)
anomaly_u850 = u850.get_doys_in_span(shorter_u850, ncfile_u850_path, day_start, day_end)
interpolated_u850 = u850.interpolate_spatial_grid_to_original(anomaly_u850)
#******************************#
print(interpolated_olr.olr)
print(type(interpolated_olr.olr))
#******  Find PC  ******#
#solver = MultivariateEof([anomaly_olr.olr, anomaly_u200.u200, anomaly_u850.u850])
solver = MultivariateEof([interpolated_olr.olr, interpolated_u200.u200, interpolated_u850.u850])
pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1))

pc1, pc2 = [], []
for pc in pcs:
    pc1.append(pc[0])
    pc2.append(pc[1]) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
df = pd.DataFrame({"Date": dates, "PC1": pc1, "PC2": pc2})
df.to_csv(pctxtfile, index=False, float_format="%.5f")
#**********************#
print("--- %s seconds totally ---" % (time.time() - start_time))
