import sys
sys.path.append("../../site-packages/mjoindices/")

import numpy as np
import pandas as pd
from pathlib import Path
import netCDF4 as netcdf4
import sst_handling as sst

#TODO take spatial_elements_amount from olr/sst data; put defs into file
def make_time_for_dataset(time, spatial_elements_amount):
    longer_time = []
    #print("length of data: ", len(data))
    for time_element in time:
        time_day_element = np.full(spatial_elements_amount, time_element ) 
        time_day_element.tolist()
        longer_time.append(time_day_element.tolist())
    longer_time = np.array(longer_time).flatten().flatten()
    return longer_time


def read_dataframe_from_file(filename: Path):
    df = pd.read_csv(sst_olr_df_path)
    return df

def sst_fill_nans(sst_restricted):
    sst_restricted_arr = sst_restricted.flatten()
    for i in range(len(sst_restricted_arr)):
        #print(i, " before ", sst_restricted_arr[i])
        if sst_restricted_arr[i] <=0:
                #print(i, " small ", sst[i])
            sst_restricted_arr[i] = np.nan
            #print(i, " after ", sst_restricted_arr[i], "\n")
    return sst_restricted_arr

def save_dataframe(filename: Path, data_list):
    print("save_dataframe:")
    df_data_out = pd.DataFrame(data_list)
    df_data_out.to_csv(filename, float_format="%.5f")
    print(df_data_out)
    
def save_sst_olr_to_df(day_start, day_end, olr_datafield, sst_datafield, olr_sst_df_file):
    spatial_elements_amount = len(olr_datafield.olr[0]) * len(olr_datafield.olr[0][0]) #spatial_elements_amount
    sst_restricted = sst_datafield.sst.flatten()
    time_restricted = sst_datafield.time.flatten()
    sst_restricted_arr = sst_fill_nans(sst_restricted)
    time_restricted_long = make_time_for_dataset(time_restricted, spatial_elements_amount)
    print(len(olr_datafield.olr.flatten()), len(sst_restricted_arr), len(time_restricted_long))
    df_data = {"day": time_restricted_long, "sst": sst_restricted_arr, "olr": olr_datafield.olr.flatten()}
    save_dataframe(olr_sst_df_file, df_data)

def save_sst_u200_to_df(day_start, day_end, u200_datafield, sst_datafield, u200_sst_df_file):
    spatial_elements_amount = len(u200_datafield.u200[0]) * len(u200_datafield.u200[0][0]) #spatial_elements_amount
    #sst_restricted, time_restricted = load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)
    sst_restricted = sst_datafield.sst.flatten()
    time_restricted = sst_datafield.time.flatten()
    #(71 144) 
    sst_restricted_arr = sst_fill_nans(sst_restricted)
    time_restricted_long = make_time_for_dataset(time_restricted, spatial_elements_amount)
    print(len(u200_datafield.u200.flatten()), len(sst_restricted_arr), len(time_restricted_long))
    # exit()
    df_data = {"day": time_restricted_long, "sst": sst_restricted_arr, "u200": u200_datafield.u200.flatten()}
    save_dataframe(u200_sst_df_file, df_data)
    
def save_sst_u850_to_df(day_start, day_end, u850_datafield, sst_datafield, u850_sst_df_file):
    spatial_elements_amount = len(u850_datafield.u850[0]) * len(u850_datafield.u850[0][0]) #spatial_elements_amount
    #sst_restricted, time_restricted = load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)
    sst_restricted = sst_datafield.sst.flatten()
    time_restricted = sst_datafield.time.flatten()
    #(71 144)
    sst_restricted_arr = sst_fill_nans(sst_restricted)
    time_restricted_long = make_time_for_dataset(time_restricted, spatial_elements_amount)
    df_data = {"day": time_restricted_long, "sst": sst_restricted_arr, "u850": u850_datafield.u850.flatten()}
    save_dataframe(u850_sst_df_file, df_data)
