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
from eofs.standard import Eof

start_time = time.time()

#TODO path+name, make file wit all paths to nc,  dependence on name, cmp7ppc for short olr 
# cut sst from everywhere, only interpolation is needed now

#1993-, 2004+, 2006, 2018 '../tests/testdata/1991-2019_2p5grid/Dec.30/'

day_start = np.datetime64("2015-01-01")
day_end = day_start + np.timedelta64(89, 'D') #89 JFM

day_start_120 = day_start - np.timedelta64(120, 'D')
day_end_120 = day_start - np.timedelta64(1, 'D')


#******  If 120 days before forecast are needed aver2 aver3  *******#
# shorter_olr_120 = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_120_path, day_start_120, day_end_120, plav=False)
# shorter_u200_120 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_120_path, day_start_120, day_end_120, plav=False)
# shorter_u850_120 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_120_path, day_start_120, day_end_120, plav=False)
# shorter_sst_120 = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start_120, day_end_120)

# interpolated_olr_120 = olr.interpolate_spatial_grid_to_original(shorter_olr_120)
# interpolated_u200_120 = u200.interpolate_spatial_grid_to_original(shorter_u200_120)
# interpolated_u850_120 = u850.interpolate_spatial_grid_to_original(shorter_u850_120)
# interpolated_sst_120 = sst.interpolate_spatial_grid_to_original(shorter_sst_120)

# save_sst_olr_to_df(day_start_120, day_end_120, interpolated_olr_120, interpolated_sst_120, olr_sst_120_df_file)
# save_sst_u200_to_df(day_start_120, day_end_120, interpolated_u200_120, interpolated_sst_120, u200_sst_120_df_file)
# save_sst_u850_to_df(day_start_120, day_end_120, interpolated_u850_120, interpolated_sst_120, u850_sst_120_df_file)

# olr_120_path = save_new_dataframe_120(olr_sst_120_df_file, "olr")
# u200_120_path = save_new_dataframe_120(u200_sst_120_df_file, "u200")
# u850_120_path = save_new_dataframe_120(u850_sst_120_df_file, "u850")
#exit()
#***************************************************************************#
# day_start = np.datetime64("2012-01-01")
day_start = np.datetime64("2015-01-01") # runmean
day_end = day_start + np.timedelta64(86, 'D') #runmean
# day_end = day_start + np.timedelta64(30, 'D') #runmean


# shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end, plav=False) #True
# shorter_u200 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_path, day_start, day_end, plav=False)
# shorter_u850 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_path, day_start, day_end, plav=False)
# shorter_sst = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)

# interpolated_olr = olr.interpolate_spatial_grid_to_original(shorter_olr)
# interpolated_u200 = u200.interpolate_spatial_grid_to_original(shorter_u200)
# interpolated_u850 = u850.interpolate_spatial_grid_to_original(shorter_u850)
# interpolated_sst = sst.interpolate_spatial_grid_to_original(shorter_sst)

# #******  Make DataFile from nc files  *******#
# save_sst_olr_to_df(day_start, day_end, interpolated_olr, interpolated_sst, olr_sst_df_file)
# save_sst_u200_to_df(day_start, day_end, interpolated_u200, interpolated_sst, u200_sst_df_file)
# save_sst_u850_to_df(day_start, day_end, interpolated_u850, interpolated_sst, u850_sst_df_file)
# #*********** If 120 days before forecast are needed aver2 aver3 **************#
# #aver 2, 3
# # df_sst_olr = get_new_dataframe(olr_sst_df_file, "olr", olr_120_path)
# # df_sst_u200 = get_new_dataframe(u200_sst_df_file, "u200", u200_120_path)
# # df_sst_u850 = get_new_dataframe(u850_sst_df_file, "u850", u850_120_path)

# #aver 
# df_sst_olr = get_new_dataframe(olr_sst_df_file, "olr")
# df_sst_u200 = get_new_dataframe(u200_sst_df_file, "u200")
# df_sst_u850 = get_new_dataframe(u850_sst_df_file, "u850")

#aver by cdo 
f = netcdf4.Dataset(ncfile_olr_path, "r")
df_sst_olr = np.array(f.variables['olr'])
print("len all olr: ", (df_sst_olr.shape))
f = netcdf4.Dataset(ncfile_u200_path, "r")
df_sst_u200 = np.array(f.variables['u'])
print("len all u200: ", (df_sst_u200.shape))
f = netcdf4.Dataset(ncfile_u850_path, "r")
df_sst_u850 = np.array(f.variables['u'])
print("len all u850: ", (df_sst_u850.shape))

f = netcdf4.Dataset(ncfile_olr_all_path, "r")
df_olr_all  = np.array(f.variables['olr'])
print("len all olr: ", (df_olr_all.shape))
f = netcdf4.Dataset(ncfile_u200_all_path, "r")
df_u200_all = np.array(f.variables['u'])
print("len all u200: ", (df_u200_all.shape))
f = netcdf4.Dataset(ncfile_u850_all_path, "r")
df_u850_all = np.array(f.variables['u'])
print("len all u850: ", (df_u850_all.shape))
#****** Calculate normalization factor  *******#


# factors from article
variance_olr  =  15.1
variance_u200 =  4.81 
variance_u850 =  1.81
# variance_olr  =  3.1
# variance_u200 =  3.81 
# variance_u850 =  1.81
variance_olr_all =  15.1 
variance_u200_all = 4.81 
variance_u850_all = 1.81

# variance_olr = np.std(df_sst_olr)
# variance_u200 = np.std(df_sst_u200)
# variance_u850 = np.std(df_sst_u850)
# # #facotrs std for all
# variance_olr_all = np.std(df_olr_all)
# variance_u200_all = np.std(df_u200_all)
# variance_u850_all = np.std(df_u850_all)


#********************************************#
print("variance_olr: ",variance_olr, " variance_u200: ", variance_u200, " variance_u850: ", variance_u850, "\n")
print("variance_olr_all: ",variance_olr_all, " variance_u200_all: ", variance_u200_all, " variance_u850_all: ", variance_u850_all, "\n")

print(df_olr_all.shape, df_u200_all.shape, df_u850_all.shape)
#******  Find PC  ******#
# solver = MultivariateEof([df_sst_olr, df_sst_u200, df_sst_u850])
# solver = MultivariateEof([df_olr_all, df_u200_all, df_u850_all])
# solver = MultivariateEof([df_sst_olr/variance_olr, df_sst_u200/variance_u200, df_sst_u850/variance_u850], center=True) # OK
# solver = MultivariateEof([df_sst_olr/variance_olr_all, df_sst_u850/variance_u200_all, df_sst_u850/variance_u850_all], center=True)
solver = MultivariateEof([df_olr_all/variance_olr_all, df_u850_all/variance_u850_all, df_u200_all/variance_u200_all], center=True)

total_variance = solver.totalAnomalyVariance()
print("total_variance: ", total_variance)
weights_list = solver.getWeights()
print("weights_list: ", weights_list)
eigenvalue1, eigenvalue2, eigenvalue3, eigenvalue4 = solver.eigenvalues(neigs=4)
print("eigenvalue1: ", eigenvalue1)
print("eigenvalue2: ", eigenvalue2)

##### !!! for WH04 _setEofWH04 in both standard.py
#7.445 7.255
eof1_list = solver.eofs(neofs=2, eofscaling=0)
file = open('eofs.txt','w')
for item in eof1_list:
    file.write(f'{item} \n')
file.close()
# exit()
print(np.array(eof1_list[0]).shape)

# pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1))
# pc1, pc2 = [], []
# for pc in pcs:
#     pc1.append(pc[0])
#     pc2.append(pc[1]) 
# dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]')
# df = pd.DataFrame({"Date": dates, "PC1": pc1, "PC2": pc2})
# df.to_csv(f'{pctxtfile}.txt', index=False, float_format="%.5f")

#TODO 
###################################################### restore fields wrom WH04
reconstruction_list = solver.reconstructedField(2) #2 because only 2 EOFS of WH04
# print(reconstruction_list)
print(np.array(reconstruction_list).shape)
ncfile = netcdf4.Dataset('my_WH.V8-testsWH.nc',mode='w',format='NETCDF4_CLASSIC')
lon_dim = ncfile.createDimension("lon", 144)
lat_dim = ncfile.createDimension("lat", 1)
time_dim = ncfile.createDimension("time", None)
ncfile.title = "test ncfile"

time = ncfile.createVariable('time', np.intc, ('time',))
time.units = 'hours since 1900-01-01'
time.long_name = 'time'
time.standard_name = "time" 
lon = ncfile.createVariable('lon', np.float64, ('lon',))
lon.units = 'degrees_east'
lon.long_name = 'longitude'
lon.standard_name = "longitude" ;
lat = ncfile.createVariable('lat', np.float64, ('lat',))
lat.units = 'degrees_north'
lat.long_name = 'latitude'
lat.standard_name = "latitude" 
olr = ncfile.createVariable('olr', np.float32, ('time', 'lat', 'lon'))
olr.units = 'J m**-2'
olr.long_name = 'Top net thermal radiation'
olr.standard_name = "toa_outgoing_longwave_flux" 

nlats = len(lat_dim); nlons = len(lon_dim);
print(nlats, nlons)
lon[:] = (2.5)*np.arange(nlons)
lat[0] = 1
time[:] = np.arange(695504, 894128, 24) #correct for 8395 days
# time[:] = np.arange(695362, 1016820, 24) # V8
# time[:] = np.arange(885916, 894128, 24)
print("len_time: ", len(time))
print(df_olr_all.shape)
print(reconstruction_list[0].shape)
olr[:] = np.array(reconstruction_list[0])

# exit()
###################################################### END restore fields wrom WH04
# find correct amplitudes
# find correct norm factors



# pseudo_pcs = np.squeeze(solver.projectField([df_sst_olr/variance_olr_all, df_sst_u200/variance_u200_all, df_sst_u850/variance_u850_all], eofscaling=1, neofs=2, weighted=True))
pseudo_pcs = np.squeeze(solver.projectField([-1*df_sst_olr/variance_olr, df_sst_u850/variance_u850, df_sst_u200/variance_u200], eofscaling=1, neofs=2, weighted=False)) # same as neofs=2
psc1, psc2 = [], []
for pc in pseudo_pcs:
    psc1.append(pc[0])#/7.445)
    psc2.append(pc[1])#/7.255) 
dates = np.arange(day_start, day_end + np.timedelta64(1, 'D'), dtype='datetime64[D]') # was 1, D
print(len(dates), len(psc1), len(psc2))
df = pd.DataFrame({"Date": dates, "PC1": psc1, "PC2": psc2}) #psc2/np.std(psc2)
df.to_csv(f'{pcstxtfile}.txt', index=False, float_format="%.5f")

# probably good
# print("pc1_std: ", np.std(psc1))
# print("pc2_std: ", np.std(psc2))
#**********************#


# #******  Find PC  ******#
# #solver = MultivariateEof([anomaly_olr.olr, anomaly_u200.u200, anomaly_u850.u850])
# solver = MultivariateEof([interpolated_olr.olr, interpolated_u200.u200, interpolated_u850.u850])
# pcs = np.squeeze(solver.pcs(npcs=2, pcscaling=1))

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

# drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', 1, 1)
# drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', 1, -1)
# drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', -1, 1)
# drawPc(f'{pctxtfile}.txt', f'{pc_png_file}', -1, -1)

drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', 1, 1)
drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', 1, -1)
drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', -1, 1)
drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', -1, -1)


# #****************************#
# print("--- %s seconds totally ---" % (time.time() - start_time))
