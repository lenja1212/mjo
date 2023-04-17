####According to file:///home/leonid/Downloads/bd9af4f9-0620-4c25-a9d2-53bf1138e448.pdf (2.3.1)  probably 
# The seasonal cycle of the wind data is removed by 
# subtracting from each grid point the time mean 							   // _ydaymean_year
# and the first three harmonics of the annual cycle of the daily climatology,
# based on the entire period of the data set

#TODO  climatology of one year?? no sense 
# 1 clim all_years 		+
# 2 data - clim 				+
# 3 clim based on all data  	+ // 1 
# 4 selyear 2015 clim  			+
# 5 lp 4
# 6 sub 2 - 5 
# ydaymean
#TODO 1979-2001 or just project

# ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc olr.day.mean.nc
## data14
cdo selyear,2014 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc		   ./ncfiles2014/era5-olr-day-2p5grid-2014.nc    
cdo selyear,2014 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc  ./ncfiles2014/era5-u200hpa-day-2p5grid-2014.nc 
cdo selyear,2014 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc  ./ncfiles2014/era5-u850hpa-day-2p5grid-2014.nc 

## data15
cdo selyear,2015 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc      	   ./ncfiles2015/era5-olr-day-2p5grid-2015.nc     
cdo selyear,2015 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc 
cdo selyear,2015 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc



cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc 		   ./era5-1979-2022/olr/era5-olr-day-2p5grid-7901.nc 		   
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-7901.nc
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-7901.nc

cdo mermean ./era5-1979-2022/olr/era5-olr-day-2p5grid-7901.nc 		  ./era5-1979-2022/olr/era5-olr-day-2p5grid-7901-merm.nc 		
cdo mermean ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-7901.nc ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-7901-merm.nc
cdo mermean ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-7901.nc ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-7901-merm.nc

 
####this step is made only to make climatoly from nnc file of 1979-2021 years (shorter above)
cdo ydaymean  -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc 		    ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n.nc
cdo ydaymean  -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc   ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n.nc
cdo ydaymean  -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc   ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n.nc


#1### Find clim for old nc files
# cdo ydaymean era5-olr-day-2p5grid.nc     ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc
# cdo ydaymean era5-u200hpa-day-2p5grid.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc
# cdo ydaymean era5-u850hpa-day-2p5grid.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc

#Same for all years and there is only one year
# cdo selyear,2021 ./anomalies_all_years/era5-olr-day-2p5grid-climt.nc      ./anomalies_all_years/era5-olr-day-2p5grid-climt-2015.nc
#2################## 1 subtract time mean  [data - clim]
cdo ydaysub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc    
cdo ydaysub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc
cdo ydaysub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc 
##############1

### Select 2015 from [data - clim] y15
cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc     ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-2015.nc    
cdo selyear,2015 ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-2015.nc
cdo selyear,2015 ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-2015.nc
#### 
### Select 2014 from [data -clim] y14
cdo selyear,2014 ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc     ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-2014.nc    
cdo selyear,2014 ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-2014.nc
cdo selyear,2014 ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-2014.nc
#### 

#3### Find clim #1####
####

# #4####### selyear 2015 clim (climatology is same for all years) so this step is not necessary 
# cdo selyear,2021   ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean.nc      ./ncfiles2015/era5-olr-day-2p5grid-clim_ydaymean-2015.nc      
# cdo selyear,20   ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-clim_ydaymean-2015.nc  
# cdo selyear,2015   ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-clim_ydaymean-2015.nc  
# ###

#5################# 2.1 find first three harmonics (year(clim)) ; [first three harmonis (yclim)]
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n.nc      ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  
###########2.1
#5################# 2.2 find first three harmonics [y2015[data - clim]] ; ft[y2015[data - clim]]
cdo lowpass,3 -del29feb ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-03lp-2015.nc    
cdo lowpass,3 -del29feb ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2015.nc
cdo lowpass,3 -del29feb ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2015.nc
###########2.2
#5################# 2.2.1 find first three harmonics [y2014[data - clim]] ; ft[y2014[data - clim]]
cdo lowpass,3 -del29feb ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-2014.nc      ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-03lp-2014.nc      
cdo lowpass,3 -del29feb ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-2014.nc  ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2014.nc   
cdo lowpass,3 -del29feb ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-2014.nc  ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2014.nc  
###########2.2.1

#6################## 3.1:  y15 - 2.1 subtract {y2015[data - clim] - [first three harmonis (yclim)]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftyclim-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftyclim-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftyclim-2015.nc
##############3.1
#6################## 3.1.1:  y15 - 2.1 subtract {y2014[data - clim] - [first three harmonis (yclim)]} #Extra
cdo sub ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-2014.nc      ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftyclim-2014.nc    
cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-2014.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftyclim-2014.nc
cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-2014.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftyclim-2014.nc
##############3.1.1
#6################## 3.2:  y15 - 2.2 subtract {y2015[data - clim] - [first three harmonis y2015[data - clim]]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-03lp-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc
##############3.2
#6################## 3.2.1:  y14 - 2.2.1 subtract {y2014[data - clim] - [first three harmonis y2014[data - clim]]} 
cdo sub ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-2014.nc     ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-03lp-2014.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc    
cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-2014.nc ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2014.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc
cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-2014.nc ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2014.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc
##############3.2.1
#6################## 3.3:  data - 2.2 subtract {y2015[data] - [first three harmonis [yclim]]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2015.nc
##############3.3
#6################## 3.3.1:  data - 2.2.1 subtract {y2014[data] - [first three harmonis [yclim]]} 
cdo sub ./ncfiles2014/era5-olr-day-2p5grid-2014.nc     ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2014.nc    
cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-2014.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-2014.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
##############3.3.1
# #6################## 3.3.V5:  data - 2.2.1 subtract {y2015[data] - [yclim]} #TODO
# cdo sub ./ncfiles2015/era5-olr-day-2p5grid-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2014.nc    
# cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
# cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
# ##############3.3V5
# #6################## 3.3.V5.1:  data - 2.2.1 subtract {y2014[data] - [yclim]]} #TODO
# cdo sub ./ncfiles2014/era5-olr-day-2p5grid-2014.nc     ./ncfiles2015/era5-olr-day-2p5grid-yclim_ydaymean-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2014.nc    
# cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-2014.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
# cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-2014.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-yclim_ydaymean-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc
# ##############3.3V5.1
#6################## 3.4:  data - 2.2 subtract {y2015[data] - [first three harmonis y2015[data - clim]]} 
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-2015.nc     ./ncfiles2015/era5-olr-day-2p5grid-subt_ydm-03lp-2015.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftydataclim-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2015.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftydataclim-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-2015.nc ./ncfiles2015/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2015.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftydataclim-2015.nc
##############3.4
#6################## 3.4.1:  data - 2.2.1 subtract {y2014[data] - [first three harmonis y2014[data - clim]]} 
cdo sub ./ncfiles2014/era5-olr-day-2p5grid-2014.nc      ./ncfiles2014/era5-olr-day-2p5grid-subt_ydm-03lp-2014.nc      ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftydataclim-2014.nc    
cdo sub ./ncfiles2014/era5-u200hpa-day-2p5grid-2014.nc  ./ncfiles2014/era5-u200hpa-day-2p5grid-subt_ydm-03lp-2014.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftydataclim-2014.nc
cdo sub ./ncfiles2014/era5-u850hpa-day-2p5grid-2014.nc  ./ncfiles2014/era5-u850hpa-day-2p5grid-subt_ydm-03lp-2014.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftydataclim-2014.nc
##############3.4.1

#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.1  {y2015[data - clim] - [first three harmonis (yclim)]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc
##############4.1
#################### 4.2  Get data 01.01.2015 - 28.03.2015 from 3.2  {y2015[data - clim] - [first three harmonis y2015[data - clim]]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc     ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc
##############4.2
#################### 4.3  Get data 01.01.2015 - 28.03.2015 from 3.3  {y2015[data] - [first three harmonis [yclim]]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc
##############4.3
#################### 4.4  Get data 01.01.2015 - 28.03.2015 from 3.4  {y2015[data] - [first three harmonis y2015[data - clim]]} 
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc
cdo seldate,2015-01-01,2015-03-28  ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc
##############4.4

# #################### 5.1 Get data 04.09.2014 - 31.12.2014 from data
cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc    
cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
# ##############5.1
# #################### 5.2 Get data 04.09.2014 - 31.12.2014 from 3.2.1 {y2014[data - clim] - [first three harmonis y2014[data - clim]]} 
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc    
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftydataclim-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc
# ##############5.2
# #################### 5.3 Get data 04.09.2014 - 31.12.2014 from 3.3.1 {y2014[data] - [first three harmonis [yclim]]} 
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftyclim-2014.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftyclim-2014.nc    
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftyclim-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc
# ##############5.3
# #################### 5.4 Get data 04.09.2014 - 31.12.2014 from 3.4.1 {y2014[data] - [first three harmonis y2014[data - clim]]} 
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-olr-day-2p5grid-ydata_sub_ftydataclim-2014.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftydataclim-2014.nc    
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u200hpa-day-2p5grid-ydata_sub_ftydataclim-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u850hpa-day-2p5grid-ydata_sub_ftydataclim-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc
# ##############5.4
# #################### 5.5 Get data 04.09.2014 - 31.12.2014 from 3.1.1 {y2014[data - clim] - [first three harmonis (yclim)]}
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-olr-day-2p5grid-ydataydm_sub_ftyclim-2014.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc    
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u200hpa-day-2p5grid-ydataydm_sub_ftyclim-2014.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc
cdo seldate,2014-09-04,2014-12-31 ./ncfiles2015/era5-u850hpa-day-2p5grid-ydataydm_sub_ftyclim-2014.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc
# ##############5.5


#Merhe data from 4 and 5  to get 210 days nc file

#################### 6.1  merge 4.1 and 5.1  2p5grid-2014-2015      //not ok 
cdo mergetime ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-ydataydm_sub_ftyclim-2015.nc    
cdo mergetime ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydataydm_sub_ftyclim-2015.nc
cdo mergetime ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydataydm_sub_ftyclim-2015.nc 
#############6.1
#################### 6.2 merge 4.1 and 5.2                          //not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc    
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc
##############6.2
#################### 6.3 merge 4.1 and 5.3 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftyclim-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
##############6.3
#################### 6.4 merge 4.1 and 5.4 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftyclim-2015.nc
##############6.4
#################### 6.5 merge 4.2 and 5.1 						//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-data-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydataydm_sub_ftdatayclim-2015.nc
##############6.5
#################### 6.6 merge 4.2 and 5.2   					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
##############6.6
#################### 6.7 merge 4.2 and 5.3 						//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
##############6.7
#################### 6.8 merge 4.2 and 5.4 						//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc
##############6.8
#################### 6.9 merge 4.3 and 5.1                      //not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-data-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydata_sub_ftyclim-2015.nc
##############6.9
#################### 6.10 merge 4.3 and 5.2 					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
##############6.10
#################### 6.11 merge 4.3 and 5.3 					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc
##############6.11
#################### 6.12 merge 4.3 and 5.4 					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
##############6.12
#################### 6.13 merge 4.4 and 5.1    					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc
##############6.13
#################### 6.14 merge 4.4 and 5.2 					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
##############6.14
#################### 6.15 merge 4.4 and 5.3 					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
##############6.15
#################### 6.16 merge 4.4 and 5.4 					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydata_sub_ftydataclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc
##############6.16
#################### 6.17 merge 4.1 and 5.5 Extra					//ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc
##############6.17
#################### 6.18 merge 4.2 and 5.5 Extra					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc
##############6.18
#################### 6.19 merge 4.3 and 5.5 Extra					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftyclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftyclim-2015.nc
##############6.19
#################### 6.20 merge 4.4 and 5.5 Extra					//not ok
cdo mergetime  ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc     ./ncfiles_120d_2014/era5-olr-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc     ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-ydata_sub_ftydataclim-2014.nc ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-ydataydm_sub_ftyclim-2014.nc ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydata_sub_ftydataclim-2015.nc
##############6.20




#################### 7.6 runmean 6.6
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc     
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc 
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc 
##############7.6
#################### 7.7 runmean 6.7 
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc              ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc      
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc          ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc          ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  
##############7.7
#################### 7.10 runmean 6.10 
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc      		   ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  		   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  		   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc
##############7.10  0
#################### 7.11 runmean 6.11 
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc       				./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc     
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc   				./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc   				./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc   
##############7.11  1
#################### 7.13 runmean 6.13
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc       						./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc        
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc   						./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc    
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-ydata_sub_ftydataclim-2015.nc   						./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc    
##############7.13  3
#################### 7.16 runmean 6.16 
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc       		./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc       
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc   		./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc  
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc   		./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc      
##############7.16
#################### 7.17 runmean 6.17
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  		    ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc       
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  		./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  		./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc      
##############7.17

#Subtract data 01.01.2015 - 28.03.2015  subtuct runmean (4. - 7.) 88day-

#################### 8.1  4.1 - 7.6   Pc/Pcs 50/-  
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc         ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom801-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom801-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom801-2015.nc
##############8.1   
#################### 8.2  4.1 - 7.7   Pc/Pcs 50/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom802-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom802-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom802-2015.nc
##############8.2    
#################### 8.3  4.1 - 7.10   Pc/Pcs 50/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom803-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom803-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom803-2015.nc 
##############8.3    
#################### 8.4  4.1 - 7.11    Pc/Pcs 50/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc         ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom804-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc     ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom804-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc     ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom804-2015.nc
##############8.4   
#################### 8.5  4.1 - 7.13   Pc/Pcs 50/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom805-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom805-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom805-2015.nc 
##############8.5   
#################### 8.6  4.1 - 7.16    Pc/Pcs 50/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom806-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom806-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom806-2015.nc 
##############8.6
#################### 8.7  4.2 - 7.6    Pc/Pcs +/+ 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom807-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom807-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom807-2015.nc
##############8.7
#################### 8.8  4.2 - 7.7    Pc/Pcs +/+ close to 8.7
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom808-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom808-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom808-2015.nc
##############8.8  
#################### 8.9  4.2 - 7.10    Pc/Pcs +/+ close to 8.8
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom809-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom809-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom809-2015.nc
##############8.9  
#################### 8.10  4.2 - 7.11     Pc/Pcs +/+ close to 8.9
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom810-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom810-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom810-2015.nc
##############8.10  
#################### 8.11  4.2 - 7.13   Pc/Pcs +/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom811-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom811-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom811-2015.nc
##############8.11
#################### 8.12  4.2 - 7.16   Pc/Pcs +/-
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom812-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom812-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom812-2015.nc
##############8.12
#################### 8.13  4.3 - 7.6    Pc/Pcs ok/ok
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom813-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom813-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom813-2015.nc
##############8.13
#################### 8.14  4.3 - 7.7    Pc/Pcs 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom814-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom814-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom814-2015.nc
##############8.14
#################### 8.15  4.3 - 7.10 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom815-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom815-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom815-2015.nc
##############8.15
#################### 8.16  4.3 - 7.11 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom816-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom816-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom816-2015.nc
##############8.16
#################### 8.17  4.3 - 7.13 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom817-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom817-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom817-2015.nc
##############8.17 
#################### 8.18  4.3 - 7.16 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom818-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom818-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom818-2015.nc
##############8.18
#################### 8.19  4.4 - 7.6
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom819-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom819-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom819-2015.nc
##############8.19
#################### 8.20  4.4 - 7.7
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom820-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom820-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydataydm_sub_ftdatayclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom820-2015.nc 
##############8.20
#################### 8.21  4.4 - 7.10
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom821-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom821-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftydataclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom821-2015.nc 
##############8.21
#################### 8.22  4.4 - 7.11
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom822-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom822-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom822-2015.nc 
##############8.22 
#################### 8.23  4.4 - 7.13
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom823-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom823-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom823-2015.nc
##############8.23
#################### 8.24  4.4 - 7.16 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom824-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom824-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftydataclim-ydata_sub_ftydataclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom824-2015.nc 
##############8.24  
#Subresult 8.4, 8.8 - good  all in odt file
#################### 8.25  4.1 - 7.17  EXTRA
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom825-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom825-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom825-2015.nc 
##############8.25  
#################### 8.26  4.2 - 7.17  EXTRA
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom826-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom826-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydataydm_sub_ftdatayclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom826-2015.nc 
##############8.26  
#################### 8.27  4.3 - 7.17  EXTRA
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom827-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom827-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom827-2015.nc 
##############8.27  
#################### 8.28  4.4 - 7.17 EXTRA
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom828-2015.nc     
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom828-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftydataclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydataydm_sub_ftyclim-ydataydm_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom828-2015.nc 
##############8.28 
#################### 8.16 V5 
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn-anom816-2015.nc    
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn-anom816-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-ydata_sub_ftyclim-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-ydata_sub_ftyclim-ydata_sub_ftyclim-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn-anom816-2015.nc
##############8.16

cdo -sellonlatbox,0.0,357.5,-15.0,15.0  ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015.nc   	 ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc    
cdo -sellonlatbox,0.0,357.5,-15.0,15.0  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc
cdo -sellonlatbox,0.0,357.5,-15.0,15.0   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc

cdo mermean  ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-zn.nc    
cdo mermean  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-zn.nc
cdo mermean  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-zn.nc


cdo fldavg ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc    
cdo fldavg ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc
cdo fldavg ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc

cdo fldstd  ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc    
cdo fldstd  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc
cdo fldstd  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc

cdo  div  ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc     -fldstd ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc    
cdo  div  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc -fldstd ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc
cdo  div  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc -fldstd ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-aver.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-st.nc

cdo zonmean  ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydmyearn2-anom816-2015-test-zn2.nc    
cdo zonmean  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydmyearn2-anom816-2015-test-zn2.nc
cdo zonmean  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom816-2015-test.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydmyearn2-anom814-2015-test-zn2.nc







###test subtruct only 120 day without other things 
#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.1  {y2015[data - clim] - [first three harmonis (yclim)]} 
cdo seldate,2015-01-01,2015-03-28  era5-olr-day-2p5grid.nc      ./ncfiles2015/era5-olr-JFMday-2p5grid-2015.nc      
cdo seldate,2015-01-01,2015-03-28  era5-u200hpa-day-2p5grid.nc  ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-2015.nc  
cdo seldate,2015-01-01,2015-03-28  era5-u850hpa-day-2p5grid.nc  ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-2015.nc  
##############4.1
# #################### 5.1 Get data 04.09.2014 - 31.12.2014 from data
cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc    
cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
# ##############5.1
#################### 6.1  merge 4.1 and 5.1  2p5grid-2014-2015 
cdo mergetime ./ncfiles2015/era5-olr-JFMday-2p5grid-2015.nc       ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-data-data-2015.nc    
cdo mergetime ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-2015.nc   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data-2015.nc
cdo mergetime ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-2015.nc   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data-2015.nc 
#############6.1
#################### 7.1 runmean 6.1
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-data-2015.nc        ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data-2015.nc    ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data-2015.nc    ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data-2015.nc
##############7.1
#################### 8.1  4.1 - 7.1
cdo sub ./ncfiles2015/era5-olr-JFMday-2p5grid-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-data-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-JFMday-2p5grid-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-data-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-JFMday-2p5grid-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-data-anom801-2015.nc
##############8.1 