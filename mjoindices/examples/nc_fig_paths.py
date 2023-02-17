

##################   tests   ################
#shorter_olr = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_path, day_start, day_end)
#interpolated_olr = olr.interpolate_spatial_grid_to_original(shorter_olr)
#shorter_sst = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start, day_end)
#interpolated_sst = sst.interpolate_spatial_grid_to_original(shorter_sst)
#save_sst_olr_to_df(day_start, day_end, interpolated_olr, interpolated_sst, olr_sst_df_file)
#exit()
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

###### cdo commands to get anomalies 
# cdo ydaymean era5-olr-day-2p5grid.nc era5-olr-day-2p5grid-clim.nc
# mv era5-olr-day-2p5grid-clim.nc ./anomalies_all_years/
# cd anomalies_all_years/
# cdo selyear,2021 era5-olr-day-2p5grid-clim.nc era5-olr-day-2p5grid-clim-2015.nc
# cdo lowpass,3 era5-olr-day-2p5grid-clim-2015.nc era5-olr-day-2p5grid-clim-2015-03lp.nc
# cd ..
# cdo selyear,2015 era5-olr-day-2p5grid.nc era5-olr-day-2p5grid-2015.nc 
# mv era5-olr-day-2p5grid-2015.nc ./ncfiles2015
# cd ./ncfiles2015
# cdo sub era5-olr-day-2p5grid-2015.nc ../anomalies_all_years/era5-olr-day-2p5grid-clim-2015-03lp.nc era5-olr-day-2p5grid-anom-2015.nc


###### all years (1991-2021) nc files
# era5-olr-day-2p5grid.nc
# era5-200hpa-day-2p5grid.nc
# era5-u850hpa-day-2p5grid.nc

######90 day files 
ncfile_olr_path = '../tests/testdata/ncfiles2015/era5-olr-day-2p5grid-anom-2015'
# ncfile_olr_path = '../tests/testdata/era5-olr-2p5grid-2015.nc' #Bare data
#ncfile_olr_path = '../tests/testdata/era5-olr-day-anom-2p5grid.nc'
#ncfile_olr_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2006.nc' #norm without sst correction
# ncfile_olr_path = '../tests/testdata/era5-olr-day-2p5grid-2015-hp.nc' # Data without climatology and first 3 harmonics 
#ncfile_olr_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-radtt-anom-2p5grid.nc' # plav
#ncfile_olr_path = '../tests131230/testdata/plv-olr-anom-day-2p5-2015.nc'

ncfile_u200_path = '../tests/testdata/ncfiles2015/era5-u200hpa-day-2p5grid-anom-2015'
# ncfile_u200_path = '../tests/testdata/era5-u200hpa-2p5grid-2015.nc' # Bare data
#ncfile_u200_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2006.nc'#norm without sst correction
# ncfile_u200_path = '../tests/testdata/era5-u200hpa-day-2p5grid-2015-hp.nc' #Data without climatology and first 3 harmonics 
#ncfile_u200_path = '../tests/testdata/erfclim.15123018-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/our-u200hpa-anom-day-2p5-2015-f3lp.nc'

ncfile_u850_path = '../tests/testdata/ncfiles2015/era5-u850hpa-day-2p5grid-anom-2015'
# ncfile_u850_path = '../tests/testdata/era5-u850hpa-2p5grid-2015.nc' # Bare data
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5-2004.nc'#norm without sst correction 
# ncfile_u850_path = '../tests/testdata/era5-u850hpa-day-2p5grid-2015-hp.nc' # Data without climatology and first 3 harmonics 
#ncfile_u850_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u850-anom-2p5grid.nc'# plav
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2006.nc'

#******  Make DataFile from nc files including 120 days before start *******#S
# day_start_120 = day_start - np.timedelta64(120, 'D')
# day_end_120 = day_start - np.timedelta64(1, 'D')

#ncfile_olr_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u200_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u850_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'

#****************   not Anomaly **********************#
ncfile_olr_120_path = '../tests/testdata/era5-olr-2p5grid-2014.nc'
ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-2p5grid-2014.nc'
ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-2p5grid-2014.nc'

# #Works Anomaly
# ncfile_olr_120_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2014.nc'
# ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2014.nc'
# ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2014.nc'

ncfile_sst_path = '../tests/testdata/era5-sst-day-2p5grid.nc'

olr_sst_df_file = 'example_data/dataframes/day_sst_olr.txt'
u200_sst_df_file = 'example_data/dataframes/day_sst_u200.txt'
u850_sst_df_file = 'example_data/dataframes/day_sst_u850.txt'

olr_sst_120_df_file = 'example_data/dataframes/day_sst_olr_120.txt'
u200_sst_120_df_file = 'example_data/dataframes/day_sst_u200_120.txt'
u850_sst_120_df_file = 'example_data/dataframes/day_sst_u850_120.txt'

pctxtfile = 'example_data/PC/PCs-JFM-2.5_120not_an_NOsst_av2_newClim_15' #PCs2-JFM-2.5_full2_aver2_NOsst_15-HP
pcstxtfile = 'example_data/PCs/PsCs-JFM-2.5_120not_an_NOsst_av2_newClim_15' #PsCs-JFM-2.5_full2_aver2_NOsst_-HP2

pc_png_file = 'example_data/Graphs/PCs-JFM-2.5_120not_an_no_sst_av2_newClim_15'
psc_png_file = 'example_data/Graphs/PsCs-JFM-2.5_120not_an_no_sst_av2_newClim_15'
