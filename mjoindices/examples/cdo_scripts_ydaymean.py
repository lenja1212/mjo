ydaymean

# cdo selyear,2015 era5-olr-day-2p5grid.nc      era5-olr-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u200hpa-day-2p5grid.nc  era5-u200hpa-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u850hpa-day-2p5grid.nc  era5-u850hpa-day-2p5grid-2015.nc 

#### Find clim
cdo ydaymean era5-olr-day-2p5grid.nc     era5-olr-day-2p5grid-clim_ydaymean.nc
cdo ydaymean era5-u200hpa-day-2p5grid.nc era5-u200hpa-day-2p5grid-clim_ydaymean.nc
cdo ydaymean era5-u850hpa-day-2p5grid.nc era5-u850hpa-day-2p5grid-clim_ydaymean.nc

mv era5-olr-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/
mv era5-u200hpa-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/
mv era5-u850hpa-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/

#Same for all years and there is only one year
# cdo selyear,2021 ./anomalies_all_years/era5-olr-day-2p5grid-clim.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim-2015.nc
#################### 1 subtract time mean  [data - clim]
cdo ydaysub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc    
cdo ydaysub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc
cdo ydaysub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc 
##############1

#################### 2.1 find first three harmonics (from data over all years) ; [first three harmonis (data)]
cdo lowpass,3 -del29feb era5-olr-day-2p5grid.nc       ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc  
cdo lowpass,3 -del29feb era5-u200hpa-day-2p5grid.nc   ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc
cdo lowpass,3 -del29feb era5-u850hpa-day-2p5grid.nc   ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc
##############2.1
#################### 2.2 find first three harmonics (from clim) (smooth climatology) ; [first three harmonis (clim)]  GOOD
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean-03lp.nc 
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean-03lp.nc 
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean-03lp.nc
##############2.2
#################### 2.3 find first three harmonics (from [data - clim] over all years) ; [first three harmonis (data - clim)]  GOOD
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm-03lp.nc  
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm-03lp.nc
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm-03lp.nc
##############2.3

# #### TEST 
# cdo selyear,2015 selyear,2015 era5-olr-day-2p5grid.nc ./ncfiles2015/era5-olr-day-2p5grid-2015.nc 
# cdo ydaymean 
# cdo lowpass,3  ./anomalies_all_years/teat-clim-2015.nc ./anomalies_all_years/teat-clim-03lp-2015.nc

# cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean-03lp.nc ./anomalies_all_years/test2-clim-2015.nc
# cdo sub ./anomalies_all_years/teat-clim-03lp-2015.nc ./anomalies_all_years/test2-clim-2015.nc ./anomalies_all_years/test-res.n
# #####

#################### 3.1 1 - 2.1 subtract {[data - clim] - [first three harmonis (data)]}  //= strange result of subtraction (olr 150-400)
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm_03lp.nc 
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm_03lp.nc
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm_03lp.nc 
##############3.1
#################### 3.2 1 - 2.2 subtract {[data - clim] - [first three harmonis (clim)]} //= strange result in step 3 (olr 150-400)  
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftcl.nc 
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftcl.nc
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftcl.nc 
##############3.2
#################### 3.3 data - 2.2 subtract {[data - [first three harmonis (clim)]}  !!! GOOD  near zero 
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc 
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc 
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc 
##############3.3 check for sub (not ydaysub -del29feb ) !same
#################### 3.4 data -  2.3 {[data - [first three harmonis (data - clim)]} !!! GODD as ftcl but near -250
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdtcl.nc 
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdtcl.nc 
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdtcl.nc  
##############3.4
#################### 3.5 1 - 2.3 subtract {[data - clim] - first three harmonis [data - clim]]} !!! GOOD  near zero (not equal 3.3)  
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdtcl.nc
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdtcl.nc
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdtcl.nc
##############3.5


# TODO
# TOTAL: 3.3, 3.5, (3.4, 3.2, 3,1)  (3.3 - like in skript) (...) ->check later

#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.3 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc       ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc 
##############4.1
#################### 4.2 Get data 01.01.2015 - 28.03.2015 from 3.5
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdtcl.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc 
##############4.2

#################### 5.1 Get data 04.09.2014 - 31.12.2014 from 3.3 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc       ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc   
##############5.1
#################### 5.2 Get data 04.09.2014 - 31.12.2014 from 3.5
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdtcl.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc  
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc 
##############5.2
#################### 5.3 Get data 04.09.2014 - 31.12.2014 from data
cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc 
cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
##############5.3 

#Merhe data from 4 and 5  to get 210 days nc file

#################### 6.1  merge 4.1 and 5.1
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc 
##############6.1
#################### 6.2 merge 4.1 and 5.2
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc 
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
##############6.2
#################### 6.3 merge 4.1 and 5.3
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc
##############6.3
#################### 6.4 merge 4.2 and 5.1
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
##############6.4
#################### 6.5 merge 4.2 and 5.2
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
##############6.5
#################### 6.6 merge 4.2 and 5.3
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc
##############6.6

#Find runmean 120

#################### 7.1 runmean 6.1
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc 
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
##############7.1
#################### 7.2 runmean 6.2
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc 
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
##############7.2
#################### 7.3 runmean 6.3
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc
##############7.3
#################### 7.4 runmean 6.4
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
##############7.4
#################### 7.5 runmean 6.5
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
##############7.5
#################### 7.6 runmean 6.6
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc
##############7.6

#Subtract data 01.01.2015 - 28.03.2015  subtuct runmean (4. - 7.)

#################### 8.1  4.1 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom801-2015.nc
##############8.1
#################### 8.2  4.1 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom802-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom802-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom802-2015.nc
##############8.2
#################### 8.3  4.1 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom803-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom803-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom803-2015.nc
##############8.3
#################### 8.4  4.1 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom804-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom804-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom804-2015.nc
##############8.4
#################### 8.5  4.1 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom805-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom805-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom805-2015.nc
##############8.5
#################### 8.6  4.1 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-anom806-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-anom806-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-anom806-2015.nc
##############8.6
#################### 8.7  4.2 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom807-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom807-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom807-2015.nc
##############8.7
#################### 8.8  4.2 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom808-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom808-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom808-2015.nc
##############8.8
#################### 8.9  4.2 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom809-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom809-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom809-2015.nc
##############8.9
#################### 8.10  4.2 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom810-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom810-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom810-2015.nc
##############8.10
#################### 8.11  4.2 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom811-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom811-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom811-2015.nc
##############8.11
#################### 8.12  4.2 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-anom812-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-anom812-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-anom812-2015.nc
##############8.12

#Sybresult 8.3, 8.6, 8.9, 8.12 - not good (5.3)