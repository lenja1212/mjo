import numpy as np
import pandas as pd
from pathlib import Path
from data_to_dataframe import *



def interpolate_sst(dataFrame):
    #interpolated_sst = dataFrame.sst.interpolate(method='linear',limit_direction='both')
    interpolated_sst = dataFrame.sst
    for i in range(len(interpolated_sst)):
        if interpolated_sst[i] <=0 or interpolated_sst[i] == np.nan:
            #print(i, " before ", interpolated_sst[i])
            
            #interpolated_sst[i] = 272.0
            interpolated_sst[i] = np.nan
            
            #print(i, " after ", interpolated_sst[i], "\n")
    #exit()
    return interpolated_sst

#def get_new_dataframe(filename: Path, field_name, df_new_field_120_data_path):
def get_new_dataframe(filename: Path, field_name):
 #TODO change filenames depends on field_name
    sst_field_df_grouped_path = f"example_data/dataframes/day_sst_grouped_days_{field_name}.txt"
    df_coefs_month_path = f"example_data/dataframes/df_coefs_month_{field_name}.txt"
    df_interpolaed_coefs_path = f"example_data/dataframes/df_interpolaed_coefs_{field_name}.txt"
    df_new_field_path = f"example_data/dataframes/df_coefs_month_new_{field_name}.txt"
    df_substracted_field_path = f"example_data/dataframes/df_data_substr_{field_name}.txt"
    df_new_field_data_path = f"example_data/dataframes/df_new_sst_{field_name}.txt"
    df_new_field_data_arrayed_path =  f"example_data/dataframes/df_new_arrayed_sst_{field_name}.txt"
    
    print("field: ", field_name)
    df = pd.read_csv(filename)
    days = len(set(df.day))
    print("days in get_new_dataframe function: ", days)
    spatial_elements_amount = len(df)//days
    print(days, spatial_elements_amount)
    group_dataframe_by_days(df, field_name, days, spatial_elements_amount, sst_field_df_grouped_path)# NOsst
    #find_coefs_lin_regression(sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_coefs_month_path, df_interpolaed_coefs_path) #nsst 0-3 
    #find_coefs_lin_regression(sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_coefs_month_path, df_interpolaed_coefs_path) #nsst 4
    #make_new_field_data(sst_field_df_grouped_path, df_interpolaed_coefs_path, field_name, df_new_field_path) #nsst 0-3 
    
    #substract_120_average(df_new_field_120_data_path, sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_substracted_field_path)# NOsst
    #substract_120_average(df_new_field_120_data_path, df_interpolaed_coefs_path, field_name, days, spatial_elements_amount, df_substracted_field_path)#nsst 4
    #substract_120_average(df_new_field_120_data_path, df_new_field_path, field_name, days, spatial_elements_amount, df_substracted_field_path)
   # #substract_120_average3(df_new_field_120_data_path, df_new_field_path, field_name, days, spatial_elements_amount, df_substracted_field_path)
   
    #spat_points_to_days(df_interpolaed_coefs_path, field_name, days, spatial_elements_amount, df_new_field_data_path) # nsst 4
   # spat_points_to_days(df_new_field_path, field_name, days, spatial_elements_amount, df_new_field_data_path) #nsst 0-3 
    spat_points_to_days(sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_new_field_data_path) # opposite of group_dataframe_by_days
    #spat_points_to_days(df_substracted_field_path, field_name, days, spatial_elements_amount, df_new_field_data_path)  # 120
    
    return make_array_for_eof(df_new_field_data_path, field_name, days, spatial_elements_amount, df_new_field_data_arrayed_path) # nsst 0-4 NOstt
    #return make_array_for_eof(sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_new_field_data_arrayed_path) # nsst 0-4
    #return make_array_for_eof(filename, field_name, days, spatial_elements_amount, df_new_field_data_arrayed_path) # Nothing 

def save_new_dataframe_120(filename: Path, field_name):
    sst_field_df_grouped_path = f"example_data/dataframes/day_sst_grouped_days_120_{field_name}.txt"
    df_coefs_month_path = f"example_data/dataframes/df_coefs_month_120_{field_name}.txt"
    df_interpolaed_coefs_path = f"example_data/dataframes/df_interpolaed_coefs_120_{field_name}.txt"
    df_new_field_path = f"example_data/dataframes/df_coefs_month_new_120_{field_name}.txt"
    
    print("field_120: ", field_name)
    df = pd.read_csv(filename)
    days = len(set(df.day))
    spatial_elements_amount = len(df)//days
    print(days, spatial_elements_amount)
    
    group_dataframe_by_days(df, field_name, days, spatial_elements_amount, sst_field_df_grouped_path) #nsst 0-4
    #find_coefs_lin_regression(sst_field_df_grouped_path, field_name, days, spatial_elements_amount, df_coefs_month_path, df_interpolaed_coefs_path) #nsst 0-4
    #make_new_field_data(sst_field_df_grouped_path, df_interpolaed_coefs_path, field_name, df_new_field_path) #nsst 0-3
    #return df_new_field_path #nsst 0-3
    #return df_interpolaed_coefs_path #nsst 4
    #return filename #NOsst
    return sst_field_df_grouped_path

def group_dataframe_by_days(dataFrame, field_name, days, spatial_elements_amount, path_to_save: Path):
    print("group_dataframe_by_days")
    interpolated_sst = interpolate_sst(dataFrame)
    # print(days)
    sst_values = interpolated_sst.values
    field_values = dataFrame[field_name]
    day_values = dataFrame["day"]
    print(field_values)
    field_day_point_value = 0 
    field_day_point_array = []
    sst_day_point_value = 0
    sst_day_point_array = []
    time_day_point_array = []

    for j in range(spatial_elements_amount):
        for i in range(days): #0-92,
            field_day_point_value = field_values[j+i*spatial_elements_amount]
            sst_day_point_value = sst_values[j+i*spatial_elements_amount]
            time_day_point_array.append(day_values[i*spatial_elements_amount])
            sst_day_point_array.append(sst_day_point_value)
            field_day_point_array.append(field_day_point_value)
    new_field_data = {"day": time_day_point_array, "sst": sst_day_point_array, field_name: field_day_point_array}
    save_dataframe(path_to_save, new_field_data)
    
def find_coefs_lin_regression(filename: Path, field_name, days, spatial_elements_amount, path_to_save_df_coefs: Path, path_to_save_df_interp_coefs: Path):
    print("find_coefs_lin_regression")
    df_grouped_by_days = pd.read_csv(filename)   
    splited_time_values = np.array_split(df_grouped_by_days.day.values, spatial_elements_amount)
    splited_sst_values = np.array_split(df_grouped_by_days.sst.values, spatial_elements_amount)
    splited_field_values = np.array_split(df_grouped_by_days[field_name].values, spatial_elements_amount)
    new_data_field = []
    months_amount = days//30
    print("months: ", months_amount)
    df_coefs = pd.DataFrame(columns=('a', 'b'))
    for k in range(spatial_elements_amount):
        if k%100 == 0 or k == spatial_elements_amount-1:
            print("k: ", k, "/", spatial_elements_amount) 
        coef_b_arr = [0]*months_amount
        coef_a_arr = [0]*months_amount
            
        #time_period_name = "JFM" 
        time_period_name = days
        if time_period_name == 90:
            time_splitted_item = [splited_time_values[k][0:31], splited_time_values[k][31:59], splited_time_values[k][59:90]]
            days_splitted_item = [np.arange(0,31), np.arange(0,28), np.arange(0,31)]
        else:
            time_splitted_item = np.array_split(splited_time_values[k], months_amount).copy()
            days_splitted_item = [np.arange(0,30), np.arange(0,30), np.arange(0,30), np.arange(0,30)]
        lengths_time_splitted_item = [len(time_splitted_item[0])]
        for i in range(1, len(time_splitted_item)):
            lengths_time_splitted_item.append(len(time_splitted_item[i]) + lengths_time_splitted_item[i-1])
        sst_splitted_item = np.array_split(splited_sst_values[k], lengths_time_splitted_item).copy()
        field_splitted_item = np.array_split(splited_field_values[k], lengths_time_splitted_item).copy()
        
        #time_splitted_item = np.array_split(splited_time_values[k], months_amount).copy() # arrays with ~30 elements
        #sst_splitted_item = np.array_split(splited_sst_values[k], months_amount).copy()
        #if field_name == "olr":
            #field_splitted_item = np.array_split(np.abs(splited_field_values[k]), months_amount).copy()
        #else:
        #field_splitted_item = np.array_split(splited_field_values[k], months_amount).copy()
            
        for month in range(months_amount):
            result = np.all(sst_splitted_item[month] <= 273.0) or np.isnan(sst_splitted_item[month]).any()#or np.all(sst_splitted_item[month] == sst_splitted_item[month][0])
            if result:
#               print('All sst Values in Array are same / equal or less than 273.0')
                coef_b_arr[month] = np.nan
                coef_a_arr[month] = np.nan
            #nsst 4:    
                #print("field_splitted_item[month]: ",field_splitted_item[month])
                new_data_field = np.append(new_data_field, field_splitted_item[month])
            else:
#               print('All Values in Array are not same')
            #nsst 0-4:
                #print("field_splitted_item[month]: ",field_splitted_item[month])
                coefs = np.polyfit(sst_splitted_item[month], field_splitted_item[month], 1)
            #nsst 5:
                #coefs = np.polyfit(days_splitted_item[month], field_splitted_item[month], 1)
                coef_b_arr[month] = coefs[0]
                coef_a_arr[month] = coefs[1]
            #nsst 4:
                trendpoly = np.poly1d(coefs)
                #print("delta: ", field_splitted_item[month] - trendpoly(sst_splitted_item[month]))
                new_data_field = np.append(new_data_field, field_splitted_item[month] - trendpoly(sst_splitted_item[month]))

        #print("new_data_field: ", new_data_field)
        #exit()
        df_coefs.loc[k] = [coef_a_arr, coef_b_arr]
    df_coefs.to_csv(path_to_save_df_coefs, float_format="%.5f")
    print("days: ", days)
    print("months_amount: ", months_amount)
    #print("df_coefs:", df_coefs)
    
#sybstract data here, not in next function: like in nsst 0-3 
    print(len(df_grouped_by_days.day.values), len(df_grouped_by_days.sst.values), len(new_data_field))
    delta = {"day": df_grouped_by_days.day.values, "sst": df_grouped_by_days.sst.values, field_name: new_data_field}
    df_delta = pd.DataFrame(delta)
    df_delta.to_csv(path_to_save_df_interp_coefs, float_format="%.5f")
    
#interpolate_coefs(df_coefs, months_amount, time_splitted_item, path_to_save_df_interp_coefs) # nsst 0-3


def interpolate_coefs(df_coefs, months_amount, time_splitted_item, filename_out: Path):
    print("interpolate_coefs")
    #dataframe to check
    #df_check = pd.DataFrame(columns=('a', 'b'))
    #df_check_path ="example_data/dataframes/df_coef_months_days.txt"

    df_coefs_spat_point = pd.DataFrame(columns=('a', 'b'))
    df_indexes_amount = len(df_coefs.index)

    for i in range(df_indexes_amount):
        if i%1000 == 0 or i == df_indexes_amount-1:
            print("i:", i)
        sst_monthly_regres_coefs_a = []
        sst_monthly_regres_coefs_b = []
        df_coefs_daily = pd.DataFrame(columns=('a', 'b'))     
        
        for month in range(months_amount):
            days_in_each_month = (len(time_splitted_item[month]))
##Set coef values to middle of a month 
            #sst_daily_regres_coef_a =[np.nan]*days_in_each_month
            #sst_daily_regres_coef_b =[np.nan]*days_in_each_month
            #sst_daily_regres_coef_a[days_in_each_month//2] = df_coefs.iloc[i]['a'][month]
            #sst_daily_regres_coef_b[days_in_each_month//2] = df_coefs.iloc[i]['b'][month] 
            #sst_monthly_regres_coefs_a = np.concatenate((sst_monthly_regres_coefs_a, sst_daily_regres_coef_a))
            #sst_monthly_regres_coefs_b = np.concatenate((sst_monthly_regres_coefs_b, sst_daily_regres_coef_b))
  #Was nice          
            days_in_each_month = (len(time_splitted_item[month]))
            sst_daily_regres_coef_a = [df_coefs.iloc[i]['a'][month]] * days_in_each_month
            sst_daily_regres_coef_b = [df_coefs.iloc[i]['b'][month]] * days_in_each_month    
            sst_monthly_regres_coefs_a = np.concatenate((sst_monthly_regres_coefs_a, sst_daily_regres_coef_a))
            sst_monthly_regres_coefs_b = np.concatenate((sst_monthly_regres_coefs_b, sst_daily_regres_coef_b))  
    #        
        #df_check.loc[i] = [sst_monthly_regres_coefs_a, sst_monthly_regres_coefs_b]                                                         
        df_coefs_daily['a'] = sst_monthly_regres_coefs_a
        df_coefs_daily['b'] = sst_monthly_regres_coefs_b
        df_coefs_daily_interp = df_coefs_daily.interpolate(method='linear', limit_direction='both')
        df_coefs_spat_point = pd.concat([df_coefs_spat_point, df_coefs_daily_interp], ignore_index=True)
    #df_check.to_csv(df_check_path, float_format="%.5f")
    df_coefs_spat_point.to_csv(filename_out, float_format="%.5f")
    
def make_new_field_data(df_grouped_by_days_path: Path, df_interpolaed_coefs_path: Path, field_name, filename_out: Path):
    print("make_new_field_data")
    df_grouped_by_days = pd.read_csv(df_grouped_by_days_path)
    df_coefs_spat_point = pd.read_csv(df_interpolaed_coefs_path)
    #make new olr  #df_data_out - interpolated ingress data 
    datafield_new = []
    sst_new = df_grouped_by_days['sst'].copy()
    day_new = df_grouped_by_days['day'].copy()
    datafield_interp = 0 
    for i in range(len(df_coefs_spat_point.index)):
        a = df_coefs_spat_point.iloc[i]['a']
        b = df_coefs_spat_point.iloc[i]['b']
        datafield_interp =  a + b *  sst_new[i]
#TODO abs only for olr? in in in out out out 
        #if field_name == "olr":
            #datafield_old = np.abs(df_grouped_by_days.iloc[i][field_name])
        #else:
        datafield_old = df_grouped_by_days.iloc[i][field_name]
            
        if np.isnan(datafield_interp):
            #datafield_new.append(0.0)
            datafield_new.append(datafield_old)
        else:
            datafield_new.append(datafield_old - datafield_interp)
            
        if i%10000 == 0 or i == len(df_coefs_spat_point.index)-1:
            print("i:", i, " sst: ", sst_new[i], f"{field_name}_interp:", datafield_interp, f"{field_name}_old:", df_grouped_by_days.iloc[i][field_name],f"{field_name}_new:", datafield_new[i])
    new_field_data = {"day": day_new, "sst": sst_new, field_name: datafield_new}
    save_dataframe(filename_out, new_field_data)
    
def substract_120_average(df_new_field_120_data_path, df_new_field_path, field_name, days, spatial_elements_amount, df_substracted_field_path):
    print("substract_120_average \n")
    df = pd.read_csv(df_new_field_120_data_path)
    df90 = pd.read_csv(df_new_field_path)

    field_arr = df[field_name].values
    field_time_120 = df['day'].values
    field_arr90 = df90[field_name].values
    field_time = df90["day"].values
    field_sst = df90["sst"].values
    
    split_field_arr = np.array_split(field_arr, spatial_elements_amount)
    split_field_arr90 = np.array_split(field_arr90, spatial_elements_amount)

    days_aver = []
    for j in range(spatial_elements_amount):
        if j%100 == 0 or j == spatial_elements_amount-1:
            print("j: ", j)
        days_substracted_aver = []
        conc_arr = np.concatenate((split_field_arr[j], split_field_arr90[j]))
        for i in range(days):
            non_zero = np.count_nonzero(conc_arr[i:i+120])
            if non_zero != 0:
                average = sum(conc_arr[i:i+120])/non_zero
            else:
                print("average = 0")
                average = 0
            #if j == 0 or j == spatial_elements_amount-1:
                #print("conc_arr[i:i+120]: ", conc_arr[i:i+120])
                #print("field_time_120[i:i+120]", field_time_120[i:i+120]
                #print("non_zero: ", non_zero) 
                #print("sum: ", sum(conc_arr[i:i+120])/ non_zero) 
                #print("field: ", split_field_arr90[j][i], "average: ", average)
            #if i == 1:
                #exit()
            days_substracted_aver.append(split_field_arr90[j][i] - average)
        days_aver.append(days_substracted_aver)
    #data = {"day": field_time, "sst": field_sst, f"{field_name}_old:": np.array(split_field_arr90).flatten(), field_name: np.array(split_field_arr90).flatten()}
    data = {"day": field_time, "sst": field_sst, f"{field_name}_old:": np.array(split_field_arr90).flatten(), field_name: np.array(days_aver).flatten()}
    df_out_compare = pd.DataFrame(data)
    df_out_compare.to_csv(df_substracted_field_path)
    
def substract_120_average3(df_new_field_120_data_path, df_new_field_path, field_name, days, spatial_elements_amount, df_substracted_field_path):
    df = pd.read_csv(df_new_field_120_data_path)
    df90 = pd.read_csv(df_new_field_path)
    
    field_arr = df[field_name].values
    field_arr90 = df90[field_name].values
    field_time = df90["day"].values
    field_sst = df90["sst"].values
    
    split_field_arr = np.array_split(field_arr, spatial_elements_amount)
    split_field_arr90 = np.array_split(field_arr90, spatial_elements_amount)

    days_aver = []
    
    for j in range(spatial_elements_amount):
        if j%100 == 0 or j == spatial_elements_amount-1:
            print("j: ", j)
        days_substracted_aver = []
        conc_arr = np.concatenate((split_field_arr[j], split_field_arr90[j]))
        
        non_zero = np.count_nonzero(conc_arr[0:120])
        average = sum(conc_arr[0:120])/non_zero
        days_aver.append(split_field_arr90[j] - average)
            
        #days_aver.append(days_substracted_aver)

    data = {"day": field_time, "sst": field_sst, f"{field_name}_old:": np.array(split_field_arr90).flatten(), field_name: np.array(days_aver).flatten()}
    df_out_compare = pd.DataFrame(data)
    df_out_compare.to_csv(df_substracted_field_path)
    
    
def spat_points_to_days(df_new_field_path: Path, field_name, days, spatial_elements_amount, filename_out: Path):
    #each point to each day.
    print("spat_points_to_days")
    df = pd.read_csv(df_new_field_path)

    sst_day_point_array = []
    field_day_point_array = []
    time_day_point_array = []

    for i in range(days): #0-92
        if i%10 == 0 or i == days-1:
            print("day: ", i)
        for j in range(spatial_elements_amount):
            sst_day_point_value = df.sst[i+j*days]
            field_day_point_value = df[field_name][i+j*days]
            time_day_point_value = df.day[i+j*days]
            sst_day_point_array.append(sst_day_point_value)
            field_day_point_array.append(field_day_point_value)
            time_day_point_array.append(time_day_point_value)
    new_field_data = {"day": time_day_point_array, "sst": sst_day_point_array, field_name: field_day_point_array}
    save_dataframe(filename_out, new_field_data)
    
def make_array_for_eof(filename: Path, field_name, days, spatial_elements_amount, filename_out: Path):
    print("make_array_for_eof")
    print("spatial_elements_amount: ", spatial_elements_amount)
    df = pd.read_csv(filename)
    
    field_arr = df[field_name].values

    field_arr_d = np.array(np.array_split(field_arr, days))
    field_arr_lat = []
    for elem in field_arr_d:
        field_arr_lat.append(np.array(np.array_split(elem, spatial_elements_amount//144))) 
    field_arr_lat_lon = np.array(field_arr_lat)
    #print("field_arr_lat_lon: ",field_arr_lat_lon)
#average points over this latitude range:
    average_elem = []
    for i in range( len(field_arr_lat_lon)):
        #print("i: ", i)
        average_elem_lon = []
        for k in range( len(field_arr_lat_lon[0][0])):
            #print("k: ", k)
            average_elem_lat = []
            for j in range( len(field_arr_lat_lon[0])):
                average_elem_lat.append(field_arr_lat_lon[i][j][k])
            #print(average_elem_lat)
            summ = np.nansum(average_elem_lat)
            non_zero = np.count_nonzero(~np.isnan(average_elem_lat))
            #print("sum: ", summ, "non_zero: ", non_zero, "eq: ", summ/non_zero)
            if non_zero > 0:
                average_elem_lon.append(summ/non_zero)
            else:
                average_elem_lon.append(0.0)
            
        average_elem.append(average_elem_lon)
        #print("average_elem_lon: ", average_elem_lon)
        #print("len(average_elem_lon): ", len(average_elem_lon))
        #print("np.std: ",np.std(np.nan_to_num(np.array(average_elem))))
        #exit()
    #print("shape: ",np.array(average_elem).shape)
    #print("np.std: ",np.std(np.nan_to_num(np.array(average_elem))))
    #exit()
    return np.nan_to_num(np.array(average_elem))

    

#93
#71
#144
