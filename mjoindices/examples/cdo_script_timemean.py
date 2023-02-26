timmean
####According to file:///home/leonid/Downloads/bd9af4f9-0620-4c25-a9d2-53bf1138e448.pdf (2.3.1) timmean step is wrong 

# TODO ydaymean and after that timemean
# cdo selyear,2015 era5-olr-day-2p5grid.nc      era5-olr-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u200hpa-day-2p5grid.nc  era5-u200hpa-day-2p5grid-2015.nc 
# cdo selyear,2015 era5-u850hpa-day-2p5grid.nc  era5-u850hpa-day-2p5grid-2015.nc 

#### Find climt
cdo timmean era5-olr-day-2p5grid.nc     ./anomalies_all_years/era5-olr-day-2p5grid-climt_timmean.nc
cdo timmean era5-u200hpa-day-2p5grid.nc ./anomalies_all_years/era5-u200hpa-day-2p5grid-climt_timmean.nc
cdo timmean era5-u850hpa-day-2p5grid.nc ./anomalies_all_years/era5-u850hpa-day-2p5grid-climt_timmean.nc


#Same for all years and there is only one year
# cdo selyear,2021 ./anomalies_all_years/era5-olr-day-2p5grid-climt.nc      ./anomalies_all_years/era5-olr-day-2p5grid-climt-2015.nc
#################### 1 subtract time mean  [data - timemean]
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-climt_timmean.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc    
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-climt_timmean.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-climt_timmean.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc 
##############1

#################### 2.1 find first three harmonics (from data over all years) ; [first three harmonis (data)]
cdo lowpass,3 -del29feb era5-olr-day-2p5grid.nc       ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc  
cdo lowpass,3 -del29feb era5-u200hpa-day-2p5grid.nc   ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc
cdo lowpass,3 -del29feb era5-u850hpa-day-2p5grid.nc   ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc
##############2.1
#################### 2.2 find first three harmonics (from [data - timemean] over all years) ; [first three harmonis (data - tm)]  GOOD
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm-03lp.nc  
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm-03lp.nc
cdo lowpass,3 -del29feb ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm-03lp.nc
##############2.2

#################### 3.1:  data - 2.1 subtract {data - [first three harmonis (data)]}  good  
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_ftdata.nc    
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_ftdata.nc
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_ftdata.nc
##############3.1
#################### 3.2:  data - 2.2 subtract {data - [first three harmonis [data - timemean]]}   -350 
cdo sub era5-olr-day-2p5grid.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-data_sub_fttm_.nc     
cdo sub era5-u200hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-data_sub_fttm.nc 
cdo sub era5-u850hpa-day-2p5grid.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-data_sub_fttm.nc 
##############3.2
#################### 3.3: 1 - 2.2 subtract {[data - timemean] - [first three harmonis (data)]}  +400 
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-datatm_sub_ftdata.nc    
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datatm_sub_ftdata.nc
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datatm_sub_ftdata.nc
##############3.3
#################### 3.4: 1 - 2.2 subtract {[data - timemean] - [first three harmonis [data - timemean]]}   good
cdo sub ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc      ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm-03lp.nc      ./anomalies_all_years/era5-olr-day-2p5grid-datatm_sub_ftdatatm.nc     
cdo sub ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-subt_tm-03lp.nc  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm.nc 
cdo sub ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-subt_tm-03lp.nc  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm.nc 
##############3.4

##TEST DIFFERENT!!!
# cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm-03lp.nc  test1.nc
# cdo selyear,2015 ./anomalies_all_years/era5-olr-day-2p5grid-subt_tm.nc  test2.nc
# cdo lowpass,3 test2.nc test3.nc 
# cdo sub test1.nc test3.nc test-res.nc
###

# TODO
# TOTAL: 3.4 (3.1, 3.2, 3.3) (...) ->check later

#################### 4.1  Get data 01.01.2015 - 28.03.2015 from 3.4
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-olr-day-2p5grid-datatm_sub_ftdatatm.nc      ./ncfiles2015/era5-olr-day-2p5grid-datatm_sub_ftdatatm-2015.nc     
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm.nc  ./ncfiles2015/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc 
cdo seldate,2015-01-01,2015-03-28  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm.nc  ./ncfiles2015/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc 
##############4.1

#################### 5.1 Get data 04.09.2014 - 31.12.2014 from 3.4
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-olr-day-2p5grid-datatm_sub_ftdatatm.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datatm_sub_ftdatatm-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datatm_sub_ftdatatm-2014.nc 
cdo seldate,2014-09-04,2014-12-31  ./anomalies_all_years/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datatm_sub_ftdatatm-2014.nc   
##############5.1
# #################### 5.2 Get data 04.09.2014 - 31.12.2014 from data
# cdo seldate,2014-09-04,2014-12-31  era5-olr-day-2p5grid.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-2014.nc 
# cdo seldate,2014-09-04,2014-12-31  era5-u200hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-2014.nc
# cdo seldate,2014-09-04,2014-12-31  era5-u850hpa-day-2p5grid.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-2014.nc
# ##############5.2 

#Merhe data from 4 and 5  to get 210 days nc file

#################### 6.1  merge 4.1 and 5.1
cdo mergetime  ./ncfiles2015/era5-olr-day-2p5grid-datatm_sub_ftdatatm-2015.nc      ./ncfiles_120d_2014/era5-olr-120day-2p5grid-datatm_sub_ftdatatm-2014.nc      ./ncfiles2015/era5-olr-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc
cdo mergetime  ./ncfiles2015/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc  ./ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-datatm_sub_ftdatatm-2014.nc  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc
cdo mergetime  ./ncfiles2015/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc  ./ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-datatm_sub_ftdatatm-2014.nc  ./ncfiles2015/era5-u850hpa-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc 
#############6.1

#################### 7.1 runmean 6.1
cdo runmean,120  ./ncfiles2015/era5-olr-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc      ./ncfiles2015/era5-olr-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc 
cdo runmean,120  ./ncfiles2015/era5-u200hpa-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc  ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc
cdo runmean,120	 ./ncfiles2015/era5-u850hpa-210day-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc  ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc
##############7.1


#Subtract data 01.01.2015 - 28.03.2015  subtuct runmean (4. - 7.)

#################### 8.1  4.1 - 7.1
cdo sub ./ncfiles2015/era5-olr-day-2p5grid-datatm_sub_ftdatatm-2015.nc       ./ncfiles2015/era5-olr-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc     ./ncfiles2015/era5-olr-88day-2p5grid-datatm_sub_ftdatatm-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u200hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc   ./ncfiles2015/era5-u200hpa-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc ./ncfiles2015/era5-u200hpa-88day-2p5grid-datatm_sub_ftdatatm-anom801-2015.nc 
cdo sub ./ncfiles2015/era5-u850hpa-day-2p5grid-datatm_sub_ftdatatm-2015.nc   ./ncfiles2015/era5-u850hpa-90day_rm-2p5grid-datatm_sub_ftdatatm-datatm_sub_ftdatatm-2015.nc ./ncfiles2015/era5-u850hpa-88day-2p5grid-datatm_sub_ftdatatm-anom801-2015.nc
##############8.1

