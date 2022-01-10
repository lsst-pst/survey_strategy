#!/bin/tcsh

## This script will generate but not run the commands to concatenate mp4 files generated as movies
## of each individual opsim night, combining FilterColors/Nvisits(in each filter and all filters) using
##  'comboCommand' and outputting the list of combo videos to combine in bigMovieList.

## Note that the bigMovieList file consists of a line pointing to each mp4 file, then another pointing to
##  a special "blank.mp4" file, which is part of the git repo. The 'blank.mp4' file places a short
##  blank space between each movie night. Adding more versions of 'blank.mp4' will add a longer pause.
## Note that the bigMovieList file could be edited and the ffmpeg command rerun to change these pauses, etc.

## The 'blank.mp4' file can be re-generated (if a different size is needed, for example) by combining the logos
##  with a blank automatically generated frame from ffmpeg --
## ffmpeg -f lavfi -i color=c=white:s=965x648:d=0.7 -i lsstLogo.png -i rubinLogo.png \
## -filter_complex "[0:v] setpts=PTS-STARTPTS [background]; \
## [1:v] setpts=PTS-STARTPTS,scale=200:-1 [lsstlogo]; [2:v] setpts=PTS-STARTPTS,scale=250:-1 [rubinlogo];
## [background][lsstlogo] overlay=shortest=0:x=20:y=20 [tmp1]; [tmp1][rubinlogo] overlay=shortest=0:x=20:y=595"
## -r 30 -pix_fmt yuv420p -crf 18 -preset slower blank2.mp4


#ffmpeg -f lavfi -i color=c=white:s=2306x1078:d=1.5 -f lavfi -i color=c=black:s=2x1078:d=1.5 -i rubinlogo.png -i lsstLogo.png -filter_complex "[0:v] setpts=PTS-STARTPTS [background]; [1:v] setpts=PTS-STARTPTS [stripe]; [2:v] setpts=PTS-STARTPTS,scale=400:-1  [rubinlogo]; [3:v] setpts=PTS-STARTPTS,scale=400:-1 [lsstlogo]; [background][stripe] overlay=x=1152:y=0 [bgd]; [bgd][rubinlogo] overlay=shortest=0:x=10:y=-70 [tmp1]; [tmp1][lsstlogo]  overlay=shortest=0:x=1860:y=55" -r 30 -pix_fmt yuv420p -crf 18 -preset slower blank.mp4


## usage: expects to be run after mkOpsMovie.sh is used to generate movies for a series of individual nights.
## usage: joinOpsMovieFull.sh [opsim name] [start night] [end night]

set opsRun = $1
set nightStart = $2
set nightEnd = $3
echo "#Joining movie from " $opsRun " for nights " $nightStart " to " $nightEnd

set nights = `seq $nightStart $nightEnd`

# Set up to make FilterColors + Nvisits movie.
set combomovieList = 'bigMovieList'
set comboCommand = 'comboCommand'
if (-e $combomovieList) then
   rm $combomovieList
endif
if (-e $comboCommand) then
  rm $comboCommand
endif

echo $nights
foreach night ($nights)
 if (-e "n"$night"") then
    echo $night
    # combine NVisits and FilterColors
    # "normal" opsim movie size is 576x432
    # 8x6 image at 72*2 dpi = 1152 × 864
    #echo 'ffmpeg -f lavfi -i color=c=white:s=965x648 \' >> $comboCommand
    echo 'ffmpeg -f lavfi -i color=c=white:s=2306x1078 \' >> $comboCommand
    echo ' -f lavfi -i color=c=black:s=2x1078\'  >> $comboCommand
    echo ' -i n'$night'/FilterColors_SkyMap_30.0_30.mp4\'  >> $comboCommand
    echo ' -i n'$night'/Nvisits_SkyMap_30.0_30.mp4\'  >> $comboCommand
    echo ' -i rubinlogo.png\' >> $comboCommand
    echo ' -i lsstLogo.png\'  >> $comboCommand
    echo ' -filter_complex "[0:v] setpts=PTS-STARTPTS [background];\'  >> $comboCommand
    echo ' [1:v] setpts=PTS-STARTPTS [stripe];\'  >> $comboCommand
    echo ' [2:v] setpts=PTS-STARTPTS [pointings];\'  >> $comboCommand
    echo ' [3:v] setpts=PTS-STARTPTS,scale=1140:-1 [cumulative];\'  >> $comboCommand
    echo ' [4:v] setpts=PTS-STARTPTS,scale=400:-1 [rubinlogo];\'  >> $comboCommand
    echo ' [5:v] setpts=PTS-STARTPTS,scale=400:-1 [lsstlogo];\' >> $comboCommand
    echo ' [background][stripe] overlay=x=1152:y=0 [bgd];\'  >> $comboCommand
    echo ' [bgd][pointings] overlay=shortest=1:x=0:y=100 [tmp1];\'  >> $comboCommand
    echo ' [tmp1][cumulative] overlay=shortest=1:x=1154:y=150 [tmp2];\'  >> $comboCommand
    echo ' [tmp2][rubinlogo] overlay=shortest=0:x=10:y=-70 [tmp3];\'  >> $comboCommand
    echo ' [tmp3][lsstlogo] overlay=shortest=0:x=1860:y=55"\' >> $comboCommand
    echo ' -r 30 -pix_fmt yuv420p -crf 18 -preset slower n'$night'/combo_30.0_30.mp4' >> $comboCommand

    echo 'ffmpeg -f lavfi -i color=c=white:s=2306x1078:d=1 \' >> $comboCommand
    echo ' -f lavfi -i color=c=black:s=2x1078:d=1\'  >> $comboCommand
    echo ' -i n'$night'/FilterColors_000_SkyMap.png\'  >> $comboCommand
    echo ' -i n'$night'/Nvisits_000_SkyMap.png\'  >> $comboCommand
    echo ' -i rubinlogo.png\' >> $comboCommand
    echo ' -i lsstLogo.png\'  >> $comboCommand
    echo ' -filter_complex "[0:v] setpts=PTS-STARTPTS [background];\'  >> $comboCommand
    echo ' [1:v] setpts=PTS-STARTPTS [stripe];\'  >> $comboCommand
    echo ' [2:v] setpts=PTS-STARTPTS [pointings];\'  >> $comboCommand
    echo ' [3:v] setpts=PTS-STARTPTS,scale=1140:-1 [cumulative];\'  >> $comboCommand
    echo ' [4:v] setpts=PTS-STARTPTS,scale=400:-1 [rubinlogo];\'  >> $comboCommand
    echo ' [5:v] setpts=PTS-STARTPTS,scale=400:-1 [lsstlogo];\' >> $comboCommand
    echo ' [background][stripe] overlay=x=1152:y=0 [bgd];\'  >> $comboCommand
    echo ' [bgd][pointings] overlay=shortest=0:x=0:y=100 [tmp1];\'  >> $comboCommand
    echo ' [tmp1][cumulative] overlay=shortest=0:x=1154:y=150 [tmp2];\'  >> $comboCommand
    echo ' [tmp2][rubinlogo] overlay=shortest=0:x=10:y=-70 [tmp3];\'  >> $comboCommand
    echo ' [tmp3][lsstlogo] overlay=shortest=0:x=1860:y=55"\' >> $comboCommand
    echo ' -r 30 -pix_fmt yuv420p -crf 18 -preset slower n'$night'/start.mp4' >> $comboCommand


    set lastFilterImage=`ls n"$night"/FilterColors_*png | tail -1`
    set lastVisitImage=`ls n"$night"/Nvisits_*png | tail -1`
    echo 'ffmpeg -f lavfi -i color=c=white:s=2306x1078:d=1.5 \' >> $comboCommand
    echo ' -f lavfi -i color=c=black:s=2x1078:d=1.5\'  >> $comboCommand
    echo ' -i '$lastFilterImage'\'  >> $comboCommand
    echo ' -i '$lastVisitImage'\'  >> $comboCommand
    echo ' -i rubinlogo.png\' >> $comboCommand
    echo ' -i lsstLogo.png\'  >> $comboCommand
    echo ' -filter_complex "[0:v] setpts=PTS-STARTPTS [background];\'  >> $comboCommand
    echo ' [1:v] setpts=PTS-STARTPTS [stripe];\'  >> $comboCommand
    echo ' [2:v] setpts=PTS-STARTPTS [pointings];\'  >> $comboCommand
    echo ' [3:v] setpts=PTS-STARTPTS,scale=1140:-1 [cumulative];\'  >> $comboCommand
    echo ' [4:v] setpts=PTS-STARTPTS,scale=400:-1 [rubinlogo];\'  >> $comboCommand
    echo ' [5:v] setpts=PTS-STARTPTS,scale=400:-1 [lsstlogo];\' >> $comboCommand
    echo ' [background][stripe] overlay=x=1152:y=0 [bgd];\'  >> $comboCommand
    echo ' [bgd][pointings] overlay=shortest=0:x=0:y=100 [tmp1];\'  >> $comboCommand
    echo ' [tmp1][cumulative] overlay=shortest=0:x=1154:y=150 [tmp2];\'  >> $comboCommand
    echo ' [tmp2][rubinlogo] overlay=shortest=0:x=10:y=-70 [tmp3];\'  >> $comboCommand
    echo ' [tmp3][lsstlogo] overlay=shortest=0:x=1860:y=55"\' >> $comboCommand
    echo ' -r 30 -pix_fmt yuv420p -crf 18 -preset slower n'$night'/end.mp4' >> $comboCommand


    echo 'file n'$night'/start.mp4' >> $combomovieList
    echo 'file n'$night'/combo_30.0_30.mp4' >> $combomovieList
    echo 'file n'$night'/end.mp4' >> $combomovieList

 endif
end

echo 'file blank.mp4' >> $combomovieList

echo '# To create long movie with both FilterColors + Nvisits, over multiple nights:'
echo 'source '$comboCommand
echo 'ffmpeg -f concat -i '$combomovieList' -c copy '$opsRun'_n'$nightStart'_n'$nightEnd'.mp4'

