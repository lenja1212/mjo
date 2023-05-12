import numpy as np
import pandas as pd
import time as time_p
import sys 
import netCDF4 as netcdf4
sys.path.append("../../site-packages/mjoindices/")

import sys

from scipy.io import netcdf
from pathlib import Path

from painter import *
from nc_fig_paths import *
from eofs.multivariate.standard import MultivariateEof
from eofs.standard import Eof

start_time = time_p.time()

# normalization factors from WMO letter 
variance_olr  =  15.1
variance_u200 =  4.81 
variance_u850 =  1.81
variance_olr_all =  15.1 
variance_u200_all = 4.81 
variance_u850_all = 1.81

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
 
for hour in hours.split():
    print("hour: ",  hour)
    for member in members.split():
        print("member: ",  hour)

        ### If u want to open file directly
        ncfile_olr_path = f'{sys.argv[i]}/erfclim-olr-{anom_num}-merm-{year}-{hour}-{member}.nc'
        ncfile_u200_path = f'{sys.argv[i]}/erfclim-u200hpa-{anom_num}-merm-{year}-{hour}-{member}.nc'
        ncfile_u850_path = f'{sys.argv[i]}/erfclim-u850hpa-{anom_num}-merm-{year}-{hour}-{member}.nc'

        print(ncfile_olr_path)

        ### Names of output files and graphs
        pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-{year}-{hour}-{member}'
        pcstxtfile = f'example_data/PCs/PsCs-JFM-2.5_{pc_name}'
        psc_png_file = f'example_data/Graphs/PsCs-JFM-2.5_{pc_name}'
        
        #***************************************************************************#
        #**************************** Read procced data from files *****************#
        if (os.path.isfile(ncfile_olr_path)):   
            f = netcdf4.Dataset(ncfile_olr_path, "r")
            df_sst_olr = np.array(f.variables['olr'])
            print("len forecast olr: ", (df_sst_olr.shape))
        if (os.path.isfile(ncfile_u200_path)):   
            f = netcdf4.Dataset(ncfile_u200_path, "r")
            df_sst_u200 = np.array(f.variables['u'])
            print("len forecast u200: ", (df_sst_u200.shape))
        if (os.path.isfile(ncfile_u850_path)):   
            f = netcdf4.Dataset(ncfile_u850_path, "r")
            df_sst_u850 = np.array(f.variables['u'])
            print("len forecast u850: ", (df_sst_u850.shape))

        if (os.path.isfile(ncfile_olr_all_path)):   
            f = netcdf4.Dataset(ncfile_olr_all_path, "r")
            df_olr_all  = np.array(f.variables['olr'])
            print("len all olr: ", (df_olr_all.shape))
        if (os.path.isfile(ncfile_u200_all_path)):   
            f = netcdf4.Dataset(ncfile_u200_all_path, "r")
            df_u200_all = np.array(f.variables['u'])
            print("len all u200: ", (df_u200_all.shape))
        if (os.path.isfile(ncfile_u850_all_path)):   
            f = netcdf4.Dataset(ncfile_u850_all_path, "r")
            df_u850_all = np.array(f.variables['u'])
            print("len all u850: ", (df_u850_all.shape))

        #****** Calculate normalization factor  *******#
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

        solver = MultivariateEof([df_olr_all/variance_olr_all, df_u850_all/variance_u850_all, df_u200_all/variance_u200_all], center=True)

        #******  Find EOFS  ******# ####### NOT USED 
    
        # total_variance = solver.totalAnomalyVariance()
        # print("total_variance: ", total_variance)
        # weights_list = solver.getWeights()
        # print("weights_list: ", weights_list)
        # eigenvalue1, eigenvalue2, eigenvalue3, eigenvalue4 = solver.eigenvalues(neigs=4)
        # print("eigenvalue1: ", eigenvalue1)
        # print("eigenvalue2: ", eigenvalue2)

        # ##### !!! for WH04 _setEofWH04 in both standard.py
        eof1_list = solver.eofs(neofs=2, eofscaling=0)  #Mandatory step for correct projection on WH04 eofs
        # file = open('eofs.txt','w')
        # for item in eof1_list:
        #     file.write(f'{item} \n')
        # file.close()
        # # exit()
        # print(np.array(eof1_list[0]).shape)

        ###################################################### NOT USED - restore fields  from Pcs
        # reconstruction_list = solver.reconstructedField(2) #2 because only 2 EOFS of WH04
        # ncfile = netcdf4.Dataset('my_WH.V8-testsWH.nc',mode='w',format='NETCDF4_CLASSIC')
        # lon_dim = ncfile.createDimension("lon", 144)
        # lat_dim = ncfile.createDimension("lat", 1)
        # time_dim = ncfile.createDimension("time", None)
        # ncfile.title = "test ncfile"

        # time = ncfile.createVariable('time', np.intc, ('time',))
        # time.units = 'hours since 1900-01-01'
        # time.long_name = 'time'
        # time.standard_name = "time" 
        # lon = ncfile.createVariable('lon', np.float64, ('lon',))
        # lon.units = 'degrees_east'
        # lon.long_name = 'longitude'
        # lon.standard_name = "longitude" ;
        # lat = ncfile.createVariable('lat', np.float64, ('lat',))
        # lat.units = 'degrees_north'
        # lat.long_name = 'latitude'
        # lat.standard_name = "latitude" 
        # olr = ncfile.createVariable('olr', np.float32, ('time', 'lat', 'lon'))
        # olr.units = 'J m**-2'
        # olr.long_name = 'Top net thermal radiation'
        # olr.standard_name = "toa_outgoing_longwave_flux" 

        # nlats = len(lat_dim); nlons = len(lon_dim);
        # lon[:] = (2.5)*np.arange(nlons)
        # lat[0] = 1
        # time[:] = np.arange(695504, 894128, 24) #correct for 8395 days
        # print("len_time: ", len(time))
        # print(df_olr_all.shape)
        # print(reconstruction_list[0].shape)
        # olr[:] = np.array(reconstruction_list[0])

        # exit()
        ###################################################### END restore fields

        #******  Find PC  ******#  -1 if initial olr data are negative; 1 if olr data are positive
        pseudo_pcs = np.squeeze(solver.projectField([-1*df_sst_olr/variance_olr, df_sst_u850/variance_u850, df_sst_u200/variance_u200], eofscaling=1, neofs=2, weighted=False)) # same as neofs=2
        psc1, psc2 = [], []
        for pc in pseudo_pcs:
            psc1.append(pc[0])
            psc2.append(pc[1]) 

        df = pd.DataFrame({"PC1": psc1, "PC2": psc2}) 
        df.to_csv(f'{pcstxtfile}.txt', index=False, float_format="%.5f")

         #******  Dwar graphs  ******#
        drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', 1, 1)
        drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', 1, -1)
        drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', -1, 1)
        drawPc(f'{pcstxtfile}.txt', f'{psc_png_file}', -1, -1)

        # #****************************#
        print("--- %s seconds totally ---" % (time_p.time() - start_time))
f.close()

