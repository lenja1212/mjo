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


######90 day files 
ncfile_olr_path = '../tests/testdata/era5-olr-2p5grid-2015.nc' #N
#ncfile_olr_path = '../tests/testdata/era5-olr-day-anom-2p5grid.nc'
#ncfile_olr_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2006.nc' #norm without sst correction
# ncfile_olr_path = '../tests/testdata/era5-olr-day-2p5grid-2015-hp.nc' 
#ncfile_olr_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-radtt-anom-2p5grid.nc' # plav
#ncfile_olr_path = '../tests131230/testdata/plv-olr-anom-day-2p5-2015.nc'

ncfile_u200_path = '../tests/testdata/era5-u200hpa-2p5grid-2015.nc'
#ncfile_u200_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2006.nc'#norm without sst correction
# ncfile_u200_path = '../tests/testdata/era5-u200hpa-day-2p5grid-2015-hp.nc' 
#ncfile_u200_path = '../tests/testdata/erfclim.15123018-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u200-anom-2p5grid.nc' # plav
#ncfile_u200_path = '../tests/testdata/our-u200hpa-anom-day-2p5-2015-f3lp.nc'

ncfile_u850_path = '../tests/testdata/era5-u850hpa-2p5grid-2015.nc' # N, NN
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5-2004.nc'#norm without sst correction 
# ncfile_u850_path = '../tests/testdata/era5-u850hpa-day-2p5grid-2015-hp.nc' # f3lp hp dt
#ncfile_u850_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/erfclim.181230.ensmean-u850-anom-2p5grid.nc'# plav
#ncfile_u850_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2006.nc'

#******  Make DataFile from nc files including 120 days before start *******#S
#day_start_120 = day_start - np.timedelta64(120, 'D')
#day_end_120 = day_start - np.timedelta64(1, 'D')
#shorter_olr_120 = olr.load_noaa_interpolated_olr_netcdf4(ncfile_olr_120_path, day_start_120, day_end_120, plav=False)
#shorter_u200_120 = u200.load_noaa_interpolated_u200_netcdf4(ncfile_u200_120_path, day_start_120, day_end_120, plav=False)
#shorter_u850_120 = u850.load_noaa_interpolated_u850_netcdf4(ncfile_u850_120_path, day_start_120, day_end_120, plav=False)
#shorter_sst_120 = sst.load_noaa_interpolated_sst_netcdf4(ncfile_sst_path, day_start_120, day_end_120)

#interpolated_olr_120 = olr.interpolate_spatial_grid_to_original(shorter_olr_120)
#interpolated_u200_120 = u200.interpolate_spatial_grid_to_original(shorter_u200_120)
#interpolated_u850_120 = u850.interpolate_spatial_grid_to_original(shorter_u850_120)
#interpolated_sst_120 = sst.interpolate_spatial_grid_to_original(shorter_sst_120)


#ncfile_olr_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u200_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'
#ncfile_u850_120_path = '../tests/testdata/1991-2019_2p5grid/Dec.30/'

#****************   not Anomaly **********************#
#ncfile_olr_120_path = '../tests/testdata/era5-olr-2p5grid-2014.nc'
#ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-2p5grid-2014.nc'
#ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-2p5grid-2014.nc'

#Works Anomaly
ncfile_olr_120_path = '../tests/testdata/era5-olr-anom-day-2p5grid-2014.nc'
ncfile_u200_120_path = '../tests/testdata/era5-u200hpa-anom-day-2p5grid-2014.nc'
ncfile_u850_120_path = '../tests/testdata/era5-u850hpa-anom-day-2p5grid-2014.nc'

ncfile_sst_path = '../tests/testdata/era5-sst-day-2p5grid.nc'

olr_sst_df_file = 'example_data/dataframes/day_sst_olr.txt'
u200_sst_df_file = 'example_data/dataframes/day_sst_u200.txt'
u850_sst_df_file = 'example_data/dataframes/day_sst_u850.txt'

olr_sst_120_df_file = 'example_data/dataframes/day_sst_olr_120.txt'
u200_sst_120_df_file = 'example_data/dataframes/day_sst_u200_120.txt'
u850_sst_120_df_file = 'example_data/dataframes/day_sst_u850_120.txt'

pctxtfile = 'example_data/PC/PCs2-JFM-2.5_full2_aver2_NOsst_15-HP2'
pcstxtfile = 'example_data/PCs/PsCs-JFM-2.5_full2_aver2_NOsst_-HP2'