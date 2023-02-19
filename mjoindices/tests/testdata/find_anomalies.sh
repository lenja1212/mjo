#!/bin/bash

anom_path=./anomalies_all_years/
ncfiels_2015=./ncfiles2015
ncfiels_120d_2014=./ncfiles_120d_2014

fields="olr u200hpa u850hpa"
for field in $fields
do
	echo $field
	cdo ydaymean era5-$field-day-2p5grid.nc era5-$field-day-2p5grid-clim.nc
	mv era5-$field-day-2p5grid-clim.nc $anom_path
	cdo selyear,2021 $anom_path/era5-$field-day-2p5grid-clim.nc $anom_path/era5-$field-day-2p5grid-clim-2015.nc
	cdo lowpass,3 $anom_path/era5-$field-day-2p5grid-clim-2015.nc $anom_path/era5-$field-day-2p5grid-clim-2015-03lp.nc #is same for all years

	cdo selyear,2015 era5-$field-day-2p5grid.nc era5-$field-day-2p5grid-2015.nc 
	mv era5-$field-day-2p5grid-2015.nc $ncfiels_2015
	cdo sub $ncfiels_2015/era5-$field-day-2p5grid-2015.nc $anom_path/era5-$field-day-2p5grid-clim-2015-03lp.nc $ncfiels_2015/era5-$field-day-2p5grid-anom-2015.nc

	cdo selyear,2014 era5-$field-day-2p5grid.nc era5-$field-120day-2p5grid-2014.nc
	mv era5-$field-120day-2p5grid-2014.nc $ncfiels_120d_2014
	cdo sub $ncfiels_120d_2014/era5-$field-120day-2p5grid-2014.nc $anom_path/era5-$field-day-2p5grid-clim-2015-03lp.nc $ncfiels_120d_2014/era5-$field-120day-2p5grid-anom-2014.nc

done
