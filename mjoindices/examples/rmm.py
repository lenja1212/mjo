import numpy as np
import time
import sys 
import netCDF4 as netcdf4
sys.path.append("../../site-packages/mjoindices/")

#fish://l.kostin@77.247.240.205/home/l.kostin/.local/lib/python3.10/site-packages/mjoindices/
#data90t/geosci/rrd/slav/olr/2p5/
from scipy.io import netcdf
from pathlib import Path

import olr_handling as olr
import u200_handling as u200
import u850_handling as u850
import sst_handling as sst
from painter import *
from nc_fig_paths import *
from data_to_dataframe import *
from preanalysis import *
from eofs.multivariate.standard import MultivariateEof

start_time = time.time()

#TODO path+name, make file wit all paths to nc,  dependence on name, cmp7ppc for short olr

#1993-, 2004+, 2006, 2018 '../tests/testdata/1991-2019_2p5grid/Dec.30/'

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
solver = MultivariateEof([df_sst_olr, df_sst_u200, df_sst_u850])
# solver = MultivariateEof([df_sst_olr/variance_olr, df_sst_u200/variance_u200, df_sst_u850/variance_u850], center=True)
#solver = MultivariateEof([interpolated_olr.olr / variance_olr, interpolated_u200.u200 / variance_u200, interpolated_u850.u850 / variance_u850])
pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1))

pc1, pc2 = [], []
for pc in pcs:
    pc1.append(pc[0])
    pc2.append(pc[1]) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
df = pd.DataFrame({"Date": dates, "PC1": pc1, "PC2": pc2})
df.to_csv(f'{pctxtfile}.txt', index=False, float_format="%.5f")

pseudo_pcs = np.squeeze(solver.projectField([df_sst_olr/variance_olr, df_sst_u200/variance_u200, df_sst_u850/variance_u850], eofscaling=1, neofs=2))
psc1, psc2 = [], []
for pc in pseudo_pcs:
    psc1.append(pc[0])
    psc2.append(pc[1]) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
df = pd.DataFrame({"Date": dates, "PC1": psc1, "PC2": psc2})
df.to_csv(f'{pcstxtfile}.txt', index=False, float_format="%.5f")

#**********************#

# #******  Delete Average  ******#
# shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end)
# anomaly_olr = olr.get_doys_in_span(shorter_olr, ncfile_olr_path, day_start, day_end)
# interpolated_olr = olr.interpolate_spatial_grid_to_original(anomaly_olr)
# print("--- %s seconds for one span ---" % (time.time() - start_time))

# shorter_u200 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_path, day_start, day_end)
# anomaly_u200 = u200.get_doys_in_span(shorter_u200, ncfile_u200_path, day_start, day_end)
# interpolated_u200 = u200.interpolate_spatial_grid_to_original(anomaly_u200)

# shorter_u850 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_path, day_start, day_end)
# anomaly_u850 = u850.get_doys_in_span(shorter_u850, ncfile_u850_path, day_start, day_end)
# interpolated_u850 = u850.interpolate_spatial_grid_to_original(anomaly_u850)
# #******************************#
# print(interpolated_olr.olr)
# print(type(interpolated_olr.olr))
# #******  Find PC  ******#
# #solver = MultivariateEof([anomaly_olr.olr, anomaly_u200.u200, anomaly_u850.u850])
# solver = MultivariateEof([interpolated_olr.olr, interpolated_u200.u200, interpolated_u850.u850])
# pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1o))

# pc1, pc2 = [], []
# for pc in pcs:
#     pc1.append(pc[0])
#     pc2.append(pc[1]) 
# dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
# df = pd.DataFrame({"Date": dates, "PC1": pc1, "PC2": pc2})
# df.to_csv(f'{pctxtfile}.txt', index=False, float_format="%.5f")

#**********************#

#******  Draw PCS  ******#

# pc_png_file = 'example_data/grapgs/PCs2-JFM-2.5_full2_aver2_NOsst_15-HP2.txt'
pc_png_file = 'example_data/Graphs/PCs-JFM-2.5_no_sstdevidVar'
drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', 1, 1)
drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', 1, -1)
drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', -1, 1)
drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', -1, -1)


# #****************************#
print("--- %s seconds totally ---" % (time.time() - start_time))
