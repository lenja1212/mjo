

#############################################

#-rw-r--r-- 1 l.kostin users 9903664 Dec  8 16:49 erfclim.041230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.041230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.041230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903664 Dec  8 16:49 erfclim.061230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.061230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903616 Dec  8 16:49 erfclim.061230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903856 Dec  8 16:49 erfclim.181230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.181230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.181230.ensmean-u850-anom-2p5grid.nc

#-rw-r--r-- 1 l.kostin users 9903856 Dec  8 16:49 erfclim.931230.ensmean-radtt-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.931230.ensmean-u200-anom-2p5grid.nc
#-rw-r--r-- 1 l.kostin users 9903808 Dec  8 16:49 erfclim.931230.ensmean-u850-anom-2p5grid.nc



# 8   10.1  10.3  11 12 13 13.1
ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV13-120.nc' 		    
ncfile_u200_all_path = '../tests/testdata/era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-79-0-01-mermV13-120.nc'
ncfile_u850_all_path = '../tests/testdata/era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-79-0-01-mermV13-120.nc'
# ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV13.4-120.nc' 		    
# ncfile_u200_all_path = '../tests/testdata/era5-1979-2022/u200hpa/era5-u200hpa-day-2p5grid-79-0-01-mermV13.4-120.nc'
# ncfile_u850_all_path = '../tests/testdata/era5-1979-2022/u850hpa/era5-u850hpa-day-2p5grid-79-0-01-mermV13.4-120.nc'



# 8  (10.1) 10.2  10.3  10.4 11 12 12.1 13.4
anom_num ='anom816V13'

#good variants:
	# ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV10.1-120.nc'
	# ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV10.3-120.nc' 
	# anom_num ='anom816V8'
	# 15.1 15.1 good
	# self._flatE[0] = temp1
	# self._flatE[1] = -1*temp0

	# ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV10.1-120.nc'
	# ncfile_olr_all_path  =	   '../tests/testdata/era5-1979-2022/olr/era5-olr-day-2p5grid-79-0-01-mermV10.3-120.nc' 
	# anom_num ='anom816V10.2'
	# 15.1 15.1 good and other too
	# self._flatE[0] = temp1
	# self._flatE[1] = -1*temp0

######90 day files 								 
# ncfile_olr_path = f'../tests/testdata/ncfiles2015/era5-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2015.nc' 
# ncfile_olr_path = f'../tests/testdata/ncfiles2015/era5-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2012.nc' 
# ncfile_olr_path = f'../tests/testdata/ncfiles2015/era5-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2009.nc' 
# ncfile_olr_path = f'../tests/testdata/ncfiles2015/era5-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2008.nc' 
ncfile_olr_path = f'../tests/testdata/ncfiles2015/era5-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2006.nc' 

# ncfile_u200_path = f'../tests/testdata/ncfiles2015/era5-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2015.nc'
# ncfile_u200_path = f'../tests/testdata/ncfiles2015/era5-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2012.nc'
# ncfile_u200_path = f'../tests/testdata/ncfiles2015/era5-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2009.nc'
# ncfile_u200_path = f'../tests/testdata/ncfiles2015/era5-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2008.nc'
ncfile_u200_path = f'../tests/testdata/ncfiles2015/era5-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2006.nc'

# ncfile_u850_path = f'../tests/testdata/ncfiles2015/era5-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2015.nc'
# ncfile_u850_path = f'../tests/testdata/ncfiles2015/era5-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2012.nc'
# ncfile_u850_path = f'../tests/testdata/ncfiles2015/era5-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2009.nc'
# ncfile_u850_path = f'../tests/testdata/ncfiles2015/era5-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2008.nc'
ncfile_u850_path = f'../tests/testdata/ncfiles2015/era5-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-2006.nc'


# year='2004'
# ncfile_olr_path = f'../tests/testdata/ncfiles2015/erfclim-olr-88day-2p5grid-ydaymean-{anom_num}-grid-merm-{year}.nc'

# ncfile_u200_path = f'../tests/testdata/ncfiles2015/erfclim-u200hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-{year}.nc' 

# ncfile_u850_path = f'../tests/testdata/ncfiles2015/erfclim-u850hpa-88day-2p5grid-ydaymean-{anom_num}-grid-merm-{year}.nc' 





#******  Make DataFile from nc files including 120 days before start *******#S
# day_start_120 = day_start - np.timedelta64(120, 'D')
# day_end_120 = day_start - np.timedelta64(1, 'D')

#ncfile_olr_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u200_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u850_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'

#****************   120 days **********************#
###### not Anomaly 
# ncfile_olr_120_path = '../tests/testdata/era5-olr-2p5grid-2014.nc'
# ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-2p5grid-2014.nc'
# ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-2p5grid-2014.nc'

###### Works Anomaly
# ncfile_olr_120_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2014.nc'
# ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2014.nc'
# ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2014.nc'

##### new Anomalies
# ncfile_olr_120_path = '../tests/testdata/ncfiles_120d_2014/era5-olr-120day-2p5grid-anom-2014.nc'
# ncfile_u200_120_path = '../tests/testdata/ncfiles_120d_2014/era5-u200hpa-120day-2p5grid-anom-2014.nc'
# ncfile_u850_120_path = '../tests/testdata/ncfiles_120d_2014/era5-u850hpa-120day-2p5grid-anom-2014.nc'

# #TODO delete sst
# ncfile_sst_path = '../tests/testdata/era5-sst-day-2p5grid.nc'

# olr_sst_df_file = 'example_data/dataframes/day_sst_olr.txt'
# u200_sst_df_file = 'example_data/dataframes/day_sst_u200.txt'
# u850_sst_df_file = 'example_data/dataframes/day_sst_u850.txt'

# olr_sst_120_df_file = 'example_data/dataframes/day_sst_olr_120.txt'
# u200_sst_120_df_file = 'example_data/dataframes/day_sst_u200_120.txt'
# u850_sst_120_df_file = 'example_data/dataframes/day_sst_u850_120.txt'
#****************   no need now **********************#

pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-03123018_04' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-era2006' 

#########################################################
# pc_name = "calc-normfac-8.12-15"  #cdo_script_yadaymean
# pc_name = f'calc-normfac-clim-{anom_num}-15' #cdo_script_yadaymean version all
# pc_name = "calc-normfac-tm-8.01-15" #cdo_script_timemean
# pc_name = f'calc-normfac-ytm-{anom_num}-15' #cdo_script_timemean_year
# pc_name = f'calc-normfac-ydm-{anom_num}-15' #cdo_script_yadaymean_year
# pc_name = f'calc-normfac-ydm_data-{anom_num}-15' #cdo_script_yadaymean_year only120
# pc_name = f'calc-normfac-ydm_n-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2010 ydmyearn
# pc_name = f'calc-normfac-ydm_n2-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn
# pc_name = f'calc-normfac-ydm_n2_av2-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 average spatial articfac all below!
# pc_name = f'calc-normfac-ydm_n2_av2-zn-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 meravg
# pc_name = f'calc-normfac-ydm_n2_av2-fl-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 fldavf    #Not ok
# pc_name = f'calc-normfac-ydm_n2_av2-zn2-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 zoneman    #Not ok
# pc_name = f'calc-normfac-ydm_n2_av2-zn3-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 0-357.5 zoneman    #same good no difference 
# pc_name = f'calc-normfac-ydm_n2_av2-all20-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 20-20 0-357.5 meravg 
# pc_name = f'calc-normfac-ydm_n2_av2-all10-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 10-10 0-357.5 meravg 
# pc_name = f'calc-normfac-ydm_n2_av2-all14-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 14-14 0-357.5 meravg 
# pc_name = f'calc-normfac-ydm_n2_av2-2all14-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 14-14 0-357.5 meravg project onto all eofs #same as 2 eof
# pc_name = f'calc-normfac-ydm_n2_av2-3all14-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 14-14 0-357.5 mermean project onto all eofs   #same as meravg
# pc_name = f'calc-normfac-ydm_n2_av2-3all14-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 14-14 0-357.5 mermean project onto all eofs 
# pc_name = f'calc-normfac-ydm_n2_av2-zn-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto all eofs 
# pc_name = f'calc-normfac-ydm_n2_av2-zno-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean new olr !TODO check again later
# pc_name = f'calc-normfac-ydm_n2_av2-zne-{anom_num}-15' #cdo_script_yadaymean_year climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean  project onto eof 1979-2001
# pc_name = f'calc-normfac-ydm_n2_av2-zne2-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 

# pc_name = f'calc-normfac-ydm_n2_av2-zne3-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120  #Best
# pc_name = f'calc-normfac-ydm_n2_av2-zne3-{anom_num}-12' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120  #Good
# pc_name = f'calc-normfac-ydm_best-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120,  data artic all artic 
# pc_name = f'calc-normfac-ydm_best2-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_best3-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120, data calc all calc
# pc_name = f'calc-normfac-ydm_best4-{anom_num}-15' #cdo_script_yadaymean climatology of 1979-2001 ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2001 anom 120, data no all no #Not good

# pc_name = f'calc-normfac-ydm_v2best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1981-2010 anom 120,   data artic all artic
# pc_name = f'calc-normfac-ydm_v2best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1981-2010 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v2best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1981-2010 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v3best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v3best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v3best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v4best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 (1979-09-04-120)-2001 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v4best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 (1979-09-04-120)-2001 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v4best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 (1979-09-04-120)-2001 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v5best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v5best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v5best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v6best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v6best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v6best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2014+87 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v7best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2012+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v7best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2012+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v7best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2012+87 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v8best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2008+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v8best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2008+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v8best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2008+87 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v9best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2006+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v9best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2006+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v9best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2006+87 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v10best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2004+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v10best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2004+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v10best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2004+87 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v11best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2002+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v11best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2002+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v11best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2002+87 anom 120, data calc all calc

#make again
# pc_name = f'calc-normfac-ydm_v12best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2000+87 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v12best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2000+87 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v12best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-2000+87 anom 120, data calc all calc

#make again
# pc_name = f'calc-normfac-ydm_v13best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-120 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v13best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-120 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v13best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-120 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v14best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001-120 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v14best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001-120 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v14best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-120-2001-120 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v15best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-60 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v15best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-60 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v15best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-60 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v16best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-180 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v16best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-180 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v16best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1980-2001-180 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v17best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-120-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v17best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-120-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v17best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-120-2015+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v18best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-180-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v18best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-180-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v18best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-180-2015+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v19best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-240-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v19best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-240-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v19best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-240-2015+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v20best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-300-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v20best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-300-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v20best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2015-300-2015+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v21best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2014-0-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v21best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2014-0-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v21best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2014-0-2015+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v21best1-{anom_num}-12' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2011-0-2012+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v22best2-{anom_num}-12' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2011-0-2012+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v22best3-{anom_num}-12' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2011-0-2012+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v22best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2013-0-2015+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v22best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2013-0-2015+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v22best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 2013-0-2015+86 anom 120, data calc all calc

#EOF TEST
# pc_name = f'calc-normfac-ydm_v23best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v23best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v23best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v24best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1990-0-2012+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v24best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1990-0-2012+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v24best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1990-0-2012+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v25best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1995-0-2017+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v25best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1995-0-2017+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v25best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1995-0-2017+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v26best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1994-0-2016+86 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v26best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1994-0-2016+86 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v26best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1994-0-2016+86 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v27best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic
# pc_name = f'calc-normfac-ydm_v27best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all calc
# pc_name = f'calc-normfac-ydm_v27best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data calc all calc

# pc_name = f'calc-normfac-ydm_v28best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V3
# pc_name = f'calc-normfac-ydm_v28best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all calc  V3
# pc_name = f'calc-normfac-ydm_v28best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data calc all calc   V3

# pc_name = f'calc-normfac-ydm_v29best1-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V4
# pc_name = f'calc-normfac-ydm_v29best2-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all calc  V4
# pc_name = f'calc-normfac-ydm_v29best3-{anom_num}-15' #cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data calc all calc   V4

# pc_name = f'calc-normfac-ydm_v30best1-{anom_num}-15' #816v5 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V5
# pc_name = f'calc-normfac-ydm_v30best2-{anom_num}-15' #816v5 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all calc  V5
# pc_name = f'calc-normfac-ydm_v30best3-{anom_num}-15' #816v5 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data calc all calc   V5

# pc_name = f'calc-normfac-ydm_v31best1-{anom_num}-15' #816v6 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V6
# pc_name = f'calc-normfac-ydm_v31best2-{anom_num}-15' #816v6 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all calc  V6
# pc_name = f'calc-normfac-ydm_v31best3-{anom_num}-15' #816v6 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data calc all calc   V6

# pc_name = f'calc-normfac-ydm_v32best1-{anom_num}-15' #816V0 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V0
# pc_name = f'calc-normfac-ydm_v33best1-{anom_num}-15' #816V7 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V7
# pc_name = f'calc-normfac-ydm_v34best1-{anom_num}-15' #816V61 09-09-14-02-04-15 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V6.1
# pc_name = f'calc-normfac-ydm_v35best1-{anom_num}-15' #816V61 03-09-14-27-03-2015 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V6.2
# pc_name = f'calc-normfac-ydm_v36best1-{anom_num}-15' ##816V68 cdo_script_yadaymean climatology of all ydmyearn 15-15 0-357.5 mermean project onto eof, 15-15 1979-0-2001+0 anom 120, data artic all artic V8
# pc_name = f'calc-normfac-ydm_v37best1-{anom_num}-15' ##9 like 8 but no rumnean bot bad eofs
# pc_name = f'calc-normfac-ydm_v38best1-{anom_num}-15' ##9 like 8 but rumnean only for forcast
# pc_name = f'calc-normfac-ydm_v39best1-{anom_num}-15' ##10 all data  = 03lpclim
# pc_name = f'calc-normfac-ydm_v40best1-{anom_num}-15' ##10.1 like 8 but bandpass20-100 good eofs but forecast too smoothed 
# pc_name = f'calc-normfac-ydm_v41best1-{anom_num}-15' ##10.2 like 10.1 but forecast is not bandpass and no runmean
# pc_name = f'calc-normfac-ydm_v42best1-{anom_num}-15' ##10.3 like 10.2 but forecast is not bandpass and all with runmean
# pc_name = f'calc-normfac-ydm_v43best1-{anom_num}-15' ##10.4 like 10.3 but forecast is not bandpass and both with runmean #same as V11
# pc_name = f'calc-normfac-ydm_v44best1-{anom_num}-15' ##11 like 10.4 but forecast is not bandpass and both with runmean before bandpass # good as 10.3 but eofs should be * -1
# pc_name = f'calc-normfac-ydm_v45best1-{anom_num}-15' ##12 like 10.4 but forecast is not bandpass and all with runmean before bandpass olr data ncep# good as 10.3 but eofs should be * -1
# pc_name = f'calc-normfac-ydm_v46best1-{anom_num}-15' ##12.1 like 12 but forecast is not bandpass and both with runmean before bandpass olr data ncep# good as 10.3 but eofs should be * -1
# pc_name = f'calc-normfac-ydm_v47best1-{anom_num}-15' ##12.2 like 12 but forecast is not bandpass and forecast with runmean before bandpass olr data ncep# good as 10.3 but eofs should be * -1
# pc_name = f'calc-normfac-ydm_v48best1-{anom_num}-15' ##13 both is not bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# good

# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom

# pc_name = f'calc-normfac-ydm_v50best1-{anom_num}-15' ##13.2 like 13.1 but all is bandpass and forecast with runmean before bandpass olr data ncep; 03lp(olr-clim)#  good as 49
# pc_name = f'calc-normfac-ydm_v51best1-{anom_num}-15' ##13.3 like 13.1 but all is bandpass and forecast with runmean before bandpass olr data ncep; olr - 03lp(olr);#  not good particulary
# pc_name = f'calc-normfac-ydm_v52best1-{anom_num}-15' ##13.3 like 13.1 but all subt yearmean and forecast with runmean before bandpass olr data ncep; olr - 03lp(olr);#  not good particulary
# pc_name = f'calc-normfac-ydm_v53best1-{anom_num}-15' ##13.4 like 13.1 but all is bandpass 100 not 20-100 and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom

# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-12' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-09' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-08' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-06' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom


# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-06123000_00' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom


# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-14123000_00' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-14123000_01' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-14123000_02' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom


# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-15123000_00' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-15123000_01' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-15123000_02' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-15123000_03' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom
# pc_name = f'calc-normfac-ydm_v49best1-{anom_num}-15-15123000_04' ##13.1 like 13 but all is bandpass and both with runmean before bandpass olr data ncep; 03lp(olr-clim)# best fit with 13 anom




pctxtfile = f'example_data/PC/PCs-JFM-2.5_{pc_name}' #PCs2-JFM-2.5_full2_aver2_NOsst_15-HP
pcstxtfile = f'example_data/PCs/PsCs-JFM-2.5_{pc_name}' #PsCs-JFM-2.5_full2_aver2_NOsst_-HP2

pc_png_file = f'example_data/Graphs/PCs-JFM-2.5_{pc_name}'
psc_png_file = f'example_data/Graphs/PsCs-JFM-2.5_{pc_name}'
