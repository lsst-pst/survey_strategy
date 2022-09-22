#!/bin/csh

## This script is intended to be used as a convenience to help generate commands for making cumulative + differential movies,
## then combining the results into a single movie. Will echo, but not run, the commands.

## usage: mkDualMovies.sh [opsim name]
## (edit this file to change the sql constraint).

set opsimRun = $1

# Example of sqlconstraint & metadata for filter=r
# Because this is a somewhat stupid shell script, please provide the metadata translation of the sqlconstraint
# (i.e. the string that MAF turns your sqlconstraint into in the output images)
#set sqlconstraint = 'filter="r"'
#set metadata = 'r'

# Example of no sqlconstraint
set sqlconstraint = ''
set metadata = ''

set stepsize = 30
set nside = 64

echo "python example_movie.py "$opsimRun".db --movieStepsize "$stepsize" --nside "$nside" --ips 5 \\
  --sqlConstraint '"$sqlconstraint"' --outDir "$opsimRun"_"$sqlconstraint"_cumulative"

echo "python example_movie.py "$opsimRun".db --movieStepsize "$stepsize" --nside "$nside" --ips 5 \\
  --sqlConstraint '"$sqlconstraint"' --binned --outDir "$opsimRun"_"$sqlconstraint"_binned"

# nvisits dual movie
set metric = "N_Visits"

set movieroot = `echo $opsimRun | sed 's/\./_/g'`
set moviename = $movieroot"_"$metric"_"$metadata"_HEAL_SkyMap_5.0_5.0.mp4"
if $metadata == '' then
  set moviename = $movieroot"_"$metric"_HEAL_SkyMap_5.0_5.0.mp4"
endif

echo "ffmpeg -i "$opsimRun"_"$sqlconstraint"_cumulative/"$moviename" \\
 -i "$opsimRun"_"$sqlconstraint"_binned/"$moviename" \\
 -filter_complex 'nullsrc=size=1152x576 [background]; [0:v] setpts=PTS-STARTPTS [left]; [1:v] setpts=PTS-STARTPTS \\
 [right]; [background][left] overlay=shortest=1 [background+left]; [background+left][right] overlay=shortest=1:x=576 \\
 [left+right]' -map '[left+right]' -r 5  -pix_fmt yuv420p "$opsimRun"_"$metadata"_N_Visits.mp4"

# coadd dual movie
set metric = "Coaddm5"
set moviename = $movieroot"_"$metric"_"$metadata"_HEAL_SkyMap_5.0_5.0.mp4"
if $metadata == '' then
  set moviename = $movieroot"_"$metric"_HEAL_SkyMap_5.0_5.0.mp4"
endif

echo "ffmpeg -i "$opsimRun"_"$sqlconstraint"_cumulative/"$moviename" \\
 -i "$opsimRun"_"$sqlconstraint"_binned/"$moviename" \\
 -filter_complex 'nullsrc=size=1152x576 [background]; [0:v] setpts=PTS-STARTPTS [left]; [1:v] setpts=PTS-STARTPTS \\
 [right]; [background][left] overlay=shortest=1 [background+left]; [background+left][right] overlay=shortest=1:x=576 \\
 [left+right]' -map '[left+right]' -r 5 -pix_fmt yuv420p "$opsimRun"_"$metadata"_Coaddm5.mp4"




