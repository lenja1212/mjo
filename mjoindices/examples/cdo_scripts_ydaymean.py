ydaymean

# cdo selyear,2015 era5-olr-day-2p5grid.nc      era5-olr-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u200hpa-day-2p5grid.nc  era5-u200hpa-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u850hpa-day-2p5grid.nc  era5-u850hpa-day-2p5grid-2015.nc 

#### Find clim
# cdo ydaymean era5-olr-day-2p5grid.nc     era5-olr-day-2p5grid-clim_ydaymean.nc
# cdo ydaymean era5-u200hpa-day-2p5grid.nc era5-u200hpa-day-2p5grid-clim_ydaymean.nc
# cdo ydaymean era5-u850hpa-day-2p5grid.nc era5-u850hpa-day-2p5grid-clim_ydaymean.nc

# mv era5-olr-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/
# mv era5-u200hpa-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/
# mv era5-u850hpa-day-2p5grid-clim_ydaymean.nc ./anomalies_all_years/

################0 find climatology for 1979-2001 period
cdo ydaymean  -seldate,1979-01-01,2014-12-31 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc 		    ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n.nc
cdo ydaymean  -seldate,1979-01-01,2014-12-31 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc   ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n.nc
cdo ydaymean  -seldate,1979-01-01,2014-12-31 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc   ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n.nc
#########0

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
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_ydm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdt.nc 
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdt.nc
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_ydm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdt.nc 
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

#!!!!!#################################This snippet is needed only for projecting to eofs of 1979-2001 and has no attitude to the search of anomalies
# 0, 2.2, 3,3 
# 0  - done above 
#################### 2.2 find first three harmonics (from clim) (smooth climatology) ; [first three harmonis (clim)]  GOOD
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n.nc      ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n-03lp.nc 
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n-03lp.nc 
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n-03lp.nc
##############2.2
#################### 3.3 data - 2.2 subtract {[data - [first three harmonis (clim)]}  !!! GOOD  near zero 
cdo sub -del29feb -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/olr/era5-olr-day-2p5grid-all.nc 		  ./anomalies_all_years/era5-olr-day-2p5grid-clim_ydaymean_n-03lp.nc       ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc    
cdo sub -del29feb -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-all.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-clim_ydaymean_n-03lp.nc   ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc 
cdo sub -del29feb -seldate,1979-01-01,2001-12-31 ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-all.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-clim_ydaymean_n-03lp.nc   ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc 
##############3.3 


cdo runmean,120  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc        ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-runm.nc    
cdo runmean,120  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc    ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-runm.nc
cdo runmean,120  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc    ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-runm.nc

cdo sub -del29feb -seldate,1979-04-30,2001-12-31 ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc      ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-runm.nc     ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-sub_runm.nc    
cdo sub -del29feb -seldate,1979-04-30,2001-12-31 ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-runm.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-sub_runm.nc
cdo sub -del29feb -seldate,1979-04-30,2001-12-31 ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-runm.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-sub_runm.nc


#sub 120 
##
cdo 

#make data for MVEOF
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc     ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc      
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc
cdo mermean ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc     ./era5-1979-2022/olr/era5-olr-day-2p5grid-7901-merm.nc 		
cdo mermean ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-7901-merm.nc
cdo mermean ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdtcl-15_15-7901.nc ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-7901-merm.nc


cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-sub_runm.nc     ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-sub_runm-15-7901.nc       
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-sub_runm.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-sub_runm-15_15-7901.nc
cdo -sellonlatbox,0.0,357.5,-15.0,15.0 -seldate,1979-01-01,2001-12-31 ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-sub_runm.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-sub_runm-15_15-7901.nc
cdo mermean ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl-sub_runm-15-7901.nc        ./era5-1979-2022/olr/era5-olr-day-2p5grid-7901-merm-120.nc 		
cdo mermean ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl-sub_runm-15_15-7901.nc ./era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-7901-merm-120.nc
cdo mermean ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl-sub_runm-15_15-7901.nc ./era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-7901-merm-120.nc


#!!!!!#######

# TODO
# TOTAL: 3.3, 3.5, (3.4, 3.2, 3,1)  (3.3 - like in skript) (...) ->check later
#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.1 2015{[data - clim] - [first three harmonis (data)]}
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdt.nc       ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc     
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdt.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdt.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  
##############4.1  
#################### 4.2  Get data 01.01.2015 - 28.03.2015 from 3.2  2015{[data - clim] - [first three harmonis (clim)]}
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftcl.nc       ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftcl.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftcl.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc 
##############4.2
#################### 4.3  Get data 01.01.2015 - 28.03.2015 from 3.3  2015{[data - [first three harmonis (clim)]}
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc          ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc      ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc      ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc 
##############4.34.1
#################### 4.4  Get data 01.01.2015 - 28.03.2015 from 3.4  2015{[data - [first three harmonis (data - clim)]} 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdtcl.nc        ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdtcl.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdtcl.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc 
##############4.4
#################### 4.5 Get data 01.01.2015 - 28.03.2015 from 3.5  2015{[data - clim] - first three harmonis [data - clim]]} 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdtcl.nc      ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc    
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc 
##############4.5

#################### 5.1 Get data 04.09.2014 - 31.12.2014 from 3.1  2014{[data - clim] - [first three harmonis (data)]}
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdt.nc       ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc    
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdt.nc   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdt.nc   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc   
##############5.1
#################### 5.2 Get data 04.09.2014 - 31.12.2014 from 3.2  2014{[data - clim] - [first three harmonis (clim)]}
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftcl.nc       ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc    
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc   
##############5.2
#################### 5.3 Get data 04.09.2014 - 31.12.2014 from 3.3   2014{[data - [first three harmonis (clim)]}
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftcl.nc       ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc    
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftcl.nc   ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc   
##############5.3
#################### 5.4 Get data 04.09.2014 - 31.12.2014 from 3.4   2014{[data - [first three harmonis (data - clim)]}
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdtcl.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc    
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc   
##############5.4
#################### 5.5 Get data 04.09.2014 - 31.12.2014 from 3.5  2014{[data - clim] - first three harmonis [data - clim]]} 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-datclim_sub_ftdtcl.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc    
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datclim_sub_ftdtcl.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc 
##############5.5
#################### 5.6 Get data 04.09.2014 - 31.12.2014 from 2014data   - not good?
cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc    
cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
##############5.6


#Merhe data from 4 and 5  to get 210 days nc file
#################### 6.1  merge 4.1 and 5.1 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc    
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc 
##############6.1
#################### 6.2  merge 4.1 and 5.2 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc 
##############6.2
#################### 6.3  merge 4.1 and 5.3 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdt-2015.nc 
##############6.1
#################### 6.4  merge 4.1 and 5.4 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdt-2015.nc 
##############6.4
#################### 6.5  merge 4.1 and 5.5 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdt-2015.nc 
##############6.5
#################### 6.6  merge 4.1 and 5.6 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc                          ./ncfiles2015/era5-olr-210day-2p5grid-data-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc                      ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-datclim_sub_ftdt-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc                      ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-datclim_sub_ftdt-2015.nc 
##############6.6
#################### 6.7  merge 4.2 and 5.1 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc 
##############6.1
#################### 6.8  merge 4.2 and 5.2 							//ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc 
##############6.8
#################### 6.9  merge 4.2 and 5.3 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftcl-2015.nc 
##############6.9
#################### 6.10  merge 4.2 and 5.4 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftcl-2015.nc 
##############6.10
#################### 6.11  merge 4.2 and 5.5 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftcl-2015.nc 
##############6.11
#################### 6.12  merge 4.2 and 5.6 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-datclim_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-datclim_sub_ftcl-2015.nc 
##############6.12
#################### 6.13  merge 4.3 and 5.1 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-data_sub_ftcl-2015.nc 
##############6.13
#################### 6.14  merge 4.3 and 5.2 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-data_sub_ftcl-2015.nc 
##############6.14
#################### 6.15  merge 4.3 and 5.3 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc 
##############6.15
#################### 6.16  merge 4.3 and 5.4 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftcl-2015.nc 
##############6.16
#################### 6.17  merge 4.3 and 5.5 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc 
##############6.17
#################### 6.18  merge 4.3 and 5.6 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data_sub_ftcl-2015.nc 
##############6.18
#################### 6.19  merge 4.4 and 5.1 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-data_sub_ftdtcl-2015.nc 
##############6.19
#################### 6.20  merge 4.4 and 5.2 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-data_sub_ftdtcl-2015.nc 
##############6.20
#################### 6.21  merge 4.4 and 5.3 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftdtcl-2015.nc 
##############6.21
#################### 6.22  merge 4.4 and 5.4 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc 
##############6.22
#################### 6.23  merge 4.4 and 5.5 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftdtcl-2015.nc 
##############6.23
#################### 6.24  merge 4.4 and 5.6 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data_sub_ftdtcl-2015.nc 
##############6.24
#################### 6.25  merge 4.5 and 5.1 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdt-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdt-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdtcl-2015.nc 
##############6.25
#################### 6.26  merge 4.5 and 5.2 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdtcl-2015.nc 
##############6.26
#################### 6.27  merge 4.5 and 5.3 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc 
##############6.27
#################### 6.28  merge 4.5 and 5.4 							//not ok 
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-data_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-data_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc 
##############6.28
#################### 6.29  merge 4.5 and 5.5 							//ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datclim_sub_ftdtcl-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datclim_sub_ftdtcl-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc 
##############6.24
#################### 6.30  merge 4.5 and 5.6 							//not ok
cdo mergetime  ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc           ./ncfiles2015/era5-olr-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc    
cdo mergetime  ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc       ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-datclim_sub_ftdtcl-2015.nc 
##############6.30
#good: 6.1, 6.2, 6.7, 6.8, 6.15, 6.17, 6.22, 6,24, 6.27, 6,29

#Find runmean 120

#################### 7.1 runmean 6.1
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc
##############7.1
#################### 7.2 runmean 6.2
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc
##############7.2
#################### 7.3 runmean 6.7
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc
##############7.3
#################### 7.4 runmean 6.8
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc
##############7.4
#################### 7.5 runmean 6.15
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc            ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc
##############7.5
#################### 7.6 runmean 6.17
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc
##############7.6
#################### 7.7 runmean 6.22
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc
##############7.7
#################### 7.8 runmean 6.24
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data-data_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc
##############7.8
#################### 7.9 runmean 6.27
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc
##############7.9
#################### 7.10 runmean 6.29
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc    
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
cdo runmean,120  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc
##############7.10

#Subtract data 01.01.2015 - 28.03.2015  subtuct runmean (4. - 7.)

#################### 8.1  4.1 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom801-2015.nc
##############8.1
#################### 8.2  4.1 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom802-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom802-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom802-2015.nc
##############8.2
#################### 8.3  4.1 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom803-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom803-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom803-2015.nc
##############8.3
#################### 8.4  4.1 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom804-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom804-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom804-2015.nc
##############8.4
#################### 8.5  4.1 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc            ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom805-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom805-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom805-2015.nc
##############8.5
#################### 8.6  4.1 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom806-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom806-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom806-2015.nc
##############8.6
#################### 8.7  4.1 - 7.7
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom807-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom807-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom807-2015.nc
##############8.7
#################### 8.8  4.1 - 7.8
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc                  ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom808-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom808-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom808-2015.nc
##############8.8
#################### 8.9  4.1 - 7.9
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc          ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom809-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom809-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom809-2015.nc
##############8.9
#################### 8.10  4.1 - 7.10
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdt-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom810-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom810-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdt-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom810-2015.nc
##############8.10
#################### 8.11  4.2 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom811-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom811-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom811-2015.nc
##############8.11
#################### 8.12  4.2 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom812-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom812-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom812-2015.nc
##############8.12
#################### 8.13  4.2 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom813-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom813-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom813-2015.nc
##############8.13
#################### 8.14  4.2 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom814-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom814-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom814-2015.nc
##############8.14
#################### 8.15  4.2 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc           ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom815-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc       ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom815-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc       ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom815-2015.nc
##############8.15
#################### 8.16  4.2 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom816-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom816-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom816-2015.nc
##############8.16              
#################### 8.17  4.2 - 7.7
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom817-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom817-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom817-2015.nc
##############8.17
#################### 8.18  4.2 - 7.8
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc                  ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom818-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom818-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom818-2015.nc
##############8.18
#################### 8.19  4.2 - 7.9
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc           ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom819-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom819-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom819-2015.nc
##############8.19
#################### 8.20  4.2 - 7.10
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom820-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom820-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom820-2015.nc
##############8.20
#################### 8.21  4.3 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom821-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom821-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom821-2015.nc
##############8.21
#################### 8.22  4.3 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom822-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom822-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom822-2015.nc
##############8.22
#################### 8.23  4.3 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom823-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom823-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom823-2015.nc
##############8.23
#################### 8.24  4.3 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom824-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom824-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom824-2015.nc
##############8.24
#################### 8.25  4.3 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc            ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom825-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom825-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom825-2015.nc
##############8.25
#################### 8.26  4.3 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom826-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom826-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom826-2015.nc
##############8.26
#################### 8.27  4.3 - 7.7
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom827-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom827-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom827-2015.nc
##############8.27
#################### 8.28  4.3 - 7.8
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc                  ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom828-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom828-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom828-2015.nc
##############8.28
#################### 8.29  4.3 - 7.9
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc          ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom829-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom829-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom829-2015.nc
##############8.29
#################### 8.30  4.3 - 7.10
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom830-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom830-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom830-2015.nc
##############8.30
#################### 8.31  4.4 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc         ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom831-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc     ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom831-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc     ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom831-2015.nc
##############8.31
#################### 8.32  4.4 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom832-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom832-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom832-2015.nc
##############8.32
#################### 8.33  4.4 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom833-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom833-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom833-2015.nc
##############8.33
#################### 8.34  4.4 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom834-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom834-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom834-2015.nc
##############8.34
#################### 8.35  4.4 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc            ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom835-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom835-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom835-2015.nc
##############8.35
#################### 8.36  4.4 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom836-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom836-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom836-2015.nc
##############8.36
#################### 8.37  4.4 - 7.7
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom837-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom837-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom837-2015.nc
##############8.37
#################### 8.38  4.4 - 7.8
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc                  ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom838-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom838-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom838-2015.nc
##############8.38
#################### 8.39  4.4 - 7.9
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc         ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom839-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom839-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom839-2015.nc
##############8.39
#################### 8.40  4.4 - 7.10
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-data_sub_ftdtcl-2015.nc     ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc              ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom840-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc         ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom840-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-data_sub_ftdtcl-2015.nc ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc         ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom840-2015.nc
##############8.40
#################### 8.41  4.5 - 7.1
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom841-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom841-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom841-2015.nc
##############8.41
#################### 8.42  4.5 - 7.2
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom842-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom842-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftdt-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom842-2015.nc
##############8.42
#################### 8.43  4.5 - 7.3
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc        ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom843-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom843-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdt-datclim_sub_ftcl-2015.nc    ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom843-2015.nc
##############8.43
#################### 8.44  4.5 - 7.4
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom844-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom844-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftcl-datclim_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom844-2015.nc
##############8.44
#################### 8.45  4.5 - 7.5
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc            ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom845-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom845-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-data_sub_ftcl-2015.nc        ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom845-2015.nc
##############8.45
#################### 8.46  4.5 - 7.6
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc       ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom846-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc   ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom846-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-data_sub_ftcl-2015.nc   ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom846-2015.nc
##############8.46              
#################### 8.47  4.5 - 7.7
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom847-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom847-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftdtcl-data_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom847-2015.nc
##############8.47
#################### 8.48  4.5 - 7.8
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc                 ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom848-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc             ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom848-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data-data_sub_ftdtcl-2015.nc             ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom848-2015.nc
##############8.48
#################### 8.49  4.5 - 7.9
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc           ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom849-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom849-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-data_sub_ftcl-datclim_sub_ftdtcl-2015.nc       ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom849-2015.nc
##############8.49
#################### 8.50  4.5 - 7.10
cdo sub ./ncfiles2015/era5-olr-88day-2p5grid-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc      ./ncfiles2015/era5-olr-88day-2p5grid-ydm-anom850-2015.nc
cdo sub ./ncfiles2015/era5-u200hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u200hpa-88day-2p5grid-ydm-anom850-2015.nc
cdo sub ./ncfiles2015/era5-u850hpa-88day-2p5grid-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datclim_sub_ftdtcl-datclim_sub_ftdtcl-2015.nc  ./ncfiles2015/era5-u850hpa-88day-2p5grid-ydm-anom850-2015.nc
##############8.50