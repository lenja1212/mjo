TIMEMEAN

# cdo selyear,2015 era5-olr-day-2p5grid.nc      era5-olr-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u200hpa-day-2p5grid.nc  era5-u200hpa-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u850hpa-day-2p5grid.nc  era5-u850hpa-day-2p5grid-2015.nc 

##### cdo commands to get anomalies  (look for this step in script)
cdo timmean era5-olr-day-2p5grid.nc era5-olr-day-2p5grid-clim_timmean.nc
cdo timmean era5-u200hpa-day-2p5grid.nc era5-u200hpa-day-2p5grid-clim_timmean.nc
cdo timmean era5-u850hpa-day-2p5grid.nc era5-u850hpa-day-2p5grid-clim_timmean.nc

#there is only 2021 year 
mv era5-olr-day-2p5grid-clim_timmean.nc      ./anomalies_all_years/ 
mv era5-u200hpa-day-2p5grid-clim_timmean.nc  ./anomalies_all_years/
mv era5-u850hpa-day-2p5grid-clim_timmean.nc  ./anomalies_all_years/


## Step1 ##########  WAS 50/50
cdo sub era5-olr-day-2p5grid.nc ./anomalies_all_years/era5-olr-day-2p5grid-clim_timmean.nc ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean.nc
cdo sub era5-u200hpa-day-2p5grid.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_timmean.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-anom_timemean.nc
cdo sub era5-u850hpa-day-2p5grid.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_timmean.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-anom_timemean.nc

cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean.nc ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-2015.nc
cdo selyear,2015 ./anomalies_all_years/era5-u200hpa-day-2p5grid-anom_timemean.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-2015.nc
cdo selyear,2015 ./anomalies_all_years/era5-u850hpa-day-2p5grid-anom_timemean.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-2015.nc
## Step1 End ###### 

## Step1 ##########  version 2 
#not possible. here is only one time step
# cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-clim_timmean.nc     ./ncfiles2015/era5-olr-day-2p5grid-timemean-2015.nc
# cdo selyear,2015 ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_timmean.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-timemean-2015.nc
# cdo selyear,2015 ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_timmean.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-timemean-2015.nc
# cdo lowpass,3 ./anomalies_all_years/era5-olr-day-2p5grid-timemean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-timemean-03lp-2015.nc
# cdo lowpass,3 ./anomalies_all_years/era5-u200hpa-day-2p5grid-timemean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-timemean-03lp-2015.nc
# cdo lowpass,3 ./anomalies_all_years/era5-u850hpa-day-2p5grid-timemean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-timemean-03lp-2015.nc
# cdo sub ./ncfiles2015/era5-olr-day-2p5grid-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-timemean-03lp-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-subt_tm_03lp-2015.nc 
# cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-timemean-03lp-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm_03lp-2015.nc
# cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-timemean-03lp-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm_03lp-2015.nc

## Step1 End ###### 

## Step2 ########## check if -03lp is same  as 03hp
cdo lowpass,3 ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-03lp-2015.nc
cdo lowpass,3 ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2015.nc
cdo lowpass,3 ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2015.nc
## Step2 End ###### 

## Step2 ########## 3 harmonics of annual cycle of initial data (but not with substrcuted anomalies)
# cdo selyear,2015 era5-olr-day-2p5grid.nc     ./ncfiles2015/era5-olr-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u200hpa-day-2p5grid.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u850hpa-day-2p5grid.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc 
# cdo lowpass,3 ./ncfiles2015/era5-olr-day-2p5grid-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-03lp-2015.nc
# cdo lowpass,3 ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2015.nc
# cdo lowpass,3 ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2015.nc
## Step2 End ###### 

cdo sub ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-03lp-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-del-an_tmean_03lp-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2015.nc 

#probaly ok 
# cdo highpass,3 ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-2015.nc ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-03hp-2015.nc
#difference is sin
# cdo sub ./ncfiles2015/era5-olr-day-2p5grid-del-an_tmean_03lp-2015.nc ./ncfiles2015/era5-olr-day-2p5grid-anom_timemean-03hp-2015.nc ./ncfiles2015/era5-olr-day-2p5grid-del_hp_lp-2015.nc 

####Do the same for 2014  (delete 3 first harmonics of anual cycle for 2014)
cdo selyear,2014 ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean.nc      ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-2014.nc
cdo selyear,2014 ./anomalies_all_years/era5-u200hpa-day-2p5grid-anom_timemean.nc  ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-2014.nc
cdo selyear,2014 ./anomalies_all_years/era5-u850hpa-day-2p5grid-anom_timemean.nc  ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-2014.nc

cdo lowpass,3 ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-2014.nc      ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-03lp-2014.nc
cdo lowpass,3 ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2014.nc
cdo lowpass,3 ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2014.nc
###3 harmonics of annual cycle of initial data (but not with substrcuted anomalies)
# cdo selyear,2014 era5-olr-day-2p5grid.nc     ./ncfiles_120d_2014/era5-olr-day-2p5grid-2014.nc 
# cdo selyear,2014 era5-u200hpa-day-2p5grid.nc ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-2014.nc 
# cdo selyear,2014 era5-u850hpa-day-2p5grid.nc ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-2014.nc 

# cdo lowpass,3 ./ncfiles_120d_2014/era5-olr-day-2p5grid-2014.nc      ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-03lp-2014.nc
# cdo lowpass,3 ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2014.nc
# cdo lowpass,3 ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2014.nc




cdo sub ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-2014.nc     ./ncfiles_120d_2014/era5-olr-day-2p5grid-anom_timemean-03lp-2014.nc     ./ncfiles_120d_2014/era5-olr-day-2p5grid-del-an_tmean_03lp-2014.nc
cdo sub ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-2014.nc ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-anom_timemean-03lp-2014.nc ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2014.nc 
cdo sub ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-2014.nc ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-anom_timemean-03lp-2014.nc ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2014.nc 

#Select months from 2014 - 120days and 2015 - 90 days  ()
cdo selmon,1,2,3 ./ncfiles2015/era5-olr-day-2p5grid-del-an_tmean_03lp-2015.nc      ./ncfiles2015/era5-olr-day90-2p5grid-del-an_tmean_03lp-2015.nc
cdo selmon,1,2,3 ./ncfiles2015/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2015.nc  ./ncfiles2015/era5-u200hpa-day90-2p5grid-del-an_tmean_03lp-2015.nc
cdo selmon,1,2,3 ./ncfiles2015/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2015.nc  ./ncfiles2015/era5-u850hpa-day90-2p5grid-del-an_tmean_03lp-2015.nc

cdo selmon,9,10,11,12 ./ncfiles_120d_2014/era5-olr-day-2p5grid-del-an_tmean_03lp-2014.nc      ./ncfiles_120d_2014/era5-olr-120daye-2p5grid-del-an_tmean_03lp-2014.nc
cdo selmon,9,10,11,12 ./ncfiles_120d_2014/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120daye-2p5grid-del-an_tmean_03lp-2014.nc
cdo selmon,9,10,11,12 ./ncfiles_120d_2014/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120daye-2p5grid-del-an_tmean_03lp-2014.nc

#Merge files from step above
cdo mergetime ./ncfiles_120d_2014/era5-olr-120daye-2p5grid-del-an_tmean_03lp-2014.nc     ./ncfiles2015/era5-olr-day-2p5grid-del-an_tmean_03lp-2015.nc       ./ncfiles2015/era5-olr-210day-2p5grid-del_15-an_tmean_03lp-2015.nc
cdo mergetime ./ncfiles_120d_2014/era5-u200hpa-120daye-2p5grid-del-an_tmean_03lp-2014.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u200hpa-210day-2p5grid-del_15-an_tmean_03lp-2015.nc
cdo mergetime ./ncfiles_120d_2014/era5-u850hpa-120daye-2p5grid-del-an_tmean_03lp-2014.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u850hpa-210day-2p5grid-del_15-an_tmean_03lp-2015.nc

#####delete redundunt 3 days
cdo seldate,2014-09-04,2015-03-28 ./ncfiles2015/era5-olr-210day-2p5grid-del_15-an_tmean_03lp-2015.nc       ./ncfiles2015/era5-olr-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc   
cdo seldate,2014-09-04,2015-03-28 ./ncfiles2015/era5-u200hpa-210day-2p5grid-del_15-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u200hpa-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc
cdo seldate,2014-09-04,2015-03-28 ./ncfiles2015/era5-u850hpa-210day-2p5grid-del_15-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u850hpa-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc

##### find mean with dayrun will be 87 days  (not ydrunmean)
cdo runmean,120 ./ncfiles2015/era5-olr-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc       ./ncfiles2015/era5-olr-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc
cdo runmean,120 ./ncfiles2015/era5-u200hpa-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u200hpa-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc
cdo runmean,120 ./ncfiles2015/era5-u850hpa-210dayt-2p5grid-del_15-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u850hpa-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc 

# only for marth delete 3 last days from anomaly data and from  
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-del-an_tmean_03lp-2015.nc       ./ncfiles2015/era5-olr-87day-2p5grid-del-an_tmean_03lp-2015.nc  
cdo seldate,2014-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u200hpa-87day-2p5grid-del-an_tmean_03lp-2015.nc 
cdo seldate,2014-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u850hpa-87day-2p5grid-del-an_tmean_03lp-2015.nc 

#### Subtract from del15 runmean of 120 days before 
cdo sub ./ncfiles2015/era5-olr-87day-2p5grid-del-an_tmean_03lp-2015.nc       ./ncfiles2015/era5-olr-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-del_15_lpd15-anomf-2015.nc   
cdo sub ./ncfiles2015/era5-u200hpa-87day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u200hpa-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-del_15_lpd15-anomf-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-87day-2p5grid-del-an_tmean_03lp-2015.nc   ./ncfiles2015/era5-u850hpa-90dayt-2p5grid-del_15-an_tmean_03lp-runmean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-del_15_lpd15-anomf-2015.nc



# try check later TODO
# cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean.nc ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean-03lp.nc
# cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-anom_timemean-03lp.nc ././ncfiles2015//era5-olr-day-2p5grid-anom_timemean-03lp-2015-test.nc

##### all years (1991-2021) nc files 
era5-olr-day-2p5grid.nc
era5-200hpa-day-2p5grid.nc
era5-u850hpa-day-2p5grid.nc

