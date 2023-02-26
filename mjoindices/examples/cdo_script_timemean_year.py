####According to file:///home/leonid/Downloads/bd9af4f9-0620-4c25-a9d2-53bf1138e448.pdf (2.3.1)  probably 
# The seasonal cycle of the wind data is removed by 
# subtracting from each grid point the time mean 							   // time mean is ydaymean???  if so -> _ydaymean_year
# and the first three harmonics of the annual cycle of the daily climatology,
# based on the entire period of the data set

#TODO 
# 1 timeman all_years 		+
# 2 data - tm 				+
# 3 clim based on all data  + 
# 4 selyear 2015 clim  			+
# 5 lp 4
# 6 sub 2 - 5 
# ydaymean

## data14
cdo selyear,2014 era5-olr-day-2p5grid.nc      ./ncfiles2014/era5-olr-day-2p5grid-2014.nc 
cdo selyear,2014 era5-u200hpa-day-2p5grid.nc  ./ncfiles2014/era5-u200hpa-day-2p5grid-2014.nc 
cdo selyear,2014 era5-u850hpa-day-2p5grid.nc  ./ncfiles2014/ra5-u850hpa-day-2p5grid-2014.nc 

## data15
cdo selyear,2015 era5-olr-day-2p5grid.nc      ./ncfiles2015/era5-olr-day-2p5grid-2015.nc 
cdo selyear,2015 era5-u200hpa-day-2p5grid.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc 
cdo selyear,2015 era5-u850hpa-day-2p5grid.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc

#1### Find timeman all_years
cdo timmean era5-olr-day-2p5grid.nc     ./anomalies_all_years/era5-olr-day-2p5grid-climt_timmean.nc
cdo timmean era5-u200hpa-day-2p5grid.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-climt_timmean.nc
cdo timmean era5-u850hpa-day-2p5grid.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-climt_timmean.nc


#Same for all years and there is only one year
# cdo selyear,2021 ./anomalies_all_years/era5-olr-day-2p5grid-climt.nc      ./anomalies_all_years/era5-olr-day-2p5grid-climt-2015.nc
#2################### 1 subtract time mean  [data - timemean]
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-climt_timmean.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc    
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-climt_timmean.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-climt_timmean.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc 
##############1

### Select 2015 from [data -timemean] y15
cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc     ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-2015.nc    
cdo selyear,2015 ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-2015.nc
cdo selyear,2015 ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-2015.nc
#### 
### Select 2014 from [data -timemean] y14
cdo selyear,2014 ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc     ./ncfiles2014/era5-olr-day-2p5grid-subt_tm-2014.nc    
cdo selyear,2014 ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_tm-2014.nc
cdo selyear,2014 ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_tm-2014.nc
#### 

#3### Find clim
cdo ydaymean era5-olr-day-2p5grid.nc     ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc     
cdo ydaymean era5-u200hpa-day-2p5grid.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc
cdo ydaymean era5-u850hpa-day-2p5grid.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc
####

# #4####### selyear 2015 clim (climatology is same for all years) so this step is not necessary 
# cdo selyear,2021   ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc      ./ncfiles2015/era5-olr-day-2p5grid-clim_ydaymean-2015.nc      
# cdo selyear,20   ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-clim_ydaymean-2015.nc  
# cdo selyear,2015   ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-clim_ydaymean-2015.nc  
# ###

#5################# 2.1 find first three harmonics (year(clim)) ; [first three harmonis (yclim)]
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc      ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  
###########2.1
#5################# 2.2 find first three harmonics [y2015[data -timmean]] ; [y2015[data -timmean]]
cdo lowpass,3 -del29feb ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-03lp-2015.nc    
cdo lowpass,3 -del29feb ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-03lp-2015.nc
cdo lowpass,3 -del29feb ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-03lp-2015.nc
###########2.2
#5################# 2.2.1 find first three harmonics [y2014[data -timmean]] ; [y2014[data -timmean]]
cdo lowpass,3 -del29feb ./ncfiles2014/era5-olr-day-2p5grid-subt_tm-2014.nc      ./ncfiles2014/era5-olr-day-2p5grid-subt_tm-03lp-2014.nc      
cdo lowpass,3 -del29feb ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_tm-2014.nc  ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_tm-03lp-2014.nc   
cdo lowpass,3 -del29feb ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_tm-2014.nc  ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_tm-03lp-2014.nc  
###########2.2.1

#6################## 3.1:  y15 - 2.1 subtract {y2015[data -timmean] - [first three harmonis (yclim)]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftyclim-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftyclim-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftyclim-2015.nc
##############3.1
#6################## 3.2:  y15 - 2.2 subtract {y2015[data -timmean] - [first three harmonis y2015[data -timmean]]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-subt_tm-03lp-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_tm-03lp-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_tm-03lp-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc
##############3.2
#6################## 3.2.1:  y14 - 2.2.1 subtract {y2014[data -timmean] - [first three harmonis y2014[data -timmean]]} 
cdo sub ./ncfiles2014/era5-olr-day-2p5grid-subt_tm-2014.nc     ./ncfiles2014/era5-olr-day-2p5grid-subt_tm-03lp-2014.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc    
cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_tm-2014.nc ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_tm-03lp-2014.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc
cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_tm-2014.nc ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_tm-03lp-2014.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc
##############3.2.1
#TODO do 3.3 y2014[] - [fty2014clim]

#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.1  {y2015[data -timmean] - [first three harmonis (yclim)]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc
##############4.1
#################### 4.2  Get data 01.01.2015 - 28.03.2015 from 3.2  {y2015[data -timmean] - [first three harmonis y2015[data - timmean]]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc     ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftydatatm-2015.nc ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc
##############4.2
################ there are no hormonics in timmean

# #################### 5.1 Get data 04.09.2014 - 31.12.2014 from data
cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc 
cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
# ##############5.1
# #################### 5.2.1 Get data 04.09.2014 - 31.12.2014 from 3.2.1 {y2014[data -timmean] - [first three harmonis y2014[data -timmean]]} 
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-olr-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc    
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u200hpa-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u850hpa-day-2p5grid-ydatatm_sub_ftydatatm-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc
# ##############5.2.1 

#Merhe data from 4 and 5  to get 210 days nc file

#################### 6.1  merge 4.1 and 5.1
cdo mergetime ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc
cdo mergetime ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc
cdo mergetime ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc 
#############6.1
#################### 6.2 merge 4.1 and 5.2.1
cdo mergetime   ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc     ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc    
cdo mergetime   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc
cdo mergetime   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc
##############6.2
#################### 6.3 merge 4.2 and 5.1
cdo mergetime  ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc
cdo mergetime  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc
cdo mergetime  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc
##############6.3
#################### 6.4 merge 4.2 and 5.2.1
cdo mergetime  ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc
cdo mergetime  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc
cdo mergetime  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydatatm_sub_ftydatatm-2014.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc
##############6.4

#################### 7.1 runmean 6.1
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc
##############7.1
#################### 7.2 runmean 6.2
cdo runmean,120  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc
##############7.2
#################### 7.3 runmean 6.3
cdo runmean,120   ./ncfiles2015/era5-olr-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc    
cdo runmean,120   ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc
cdo runmean,120	  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydatatm_sub_ftydattm-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc
##############7.3
#################### 7.4 runmean 6.4
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc
##############7.4


#Subtract data 01.01.2015 - 28.03.2015  subtuct runmean (4. - 7.) 88day-

#################### 8.1  4.1 - 7.1
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom801-2015.nc
##############8.1
#################### 8.2  4.1 - 7.2
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom802-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom802-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom802-2015.nc
##############8.2
#################### 8.3  4.1 - 7.3
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom803-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom803-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom803-2015.nc
##############8.3
#################### 8.4  4.1 - 7.4
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom804-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom804-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom804-2015.nc
##############8.4
#################### 8.5  4.2 - 7.1
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom805-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom805-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom805-2015.nc
##############8.5
#################### 8.6  4.2 - 7.2
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom806-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom806-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom806-2015.nc
##############8.6
#################### 8.7  4.2 - 7.3
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom807-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom807-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom807-2015.nc
##############8.7
#################### 8.8  4.2 - 7.4
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-tmyear-anom808-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-tmyear-anom808-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydatatm_sub_ftydattm-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydatatm_sub_ftydatatm-ydatatm_sub_ftydattm-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-tmyear-anom808-2015.nc
##############8.8

#Subresult 8.1 - 8.7 - not good 
