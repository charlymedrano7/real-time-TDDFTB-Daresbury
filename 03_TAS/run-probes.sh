pumpdirs=$(ls -d phase_*)        #Where are the pumps

DFTB_PATH=/mnt/ceph/course_materials/opt/dftbplus-main/bin/dftb+ #Path to executable
nFrames=$(ls phase_0/pump_frames/*ppdump.bin | wc -l)   #Number of frames 
((nOk = $nFrames -1))                                   #defined in the dftb_in.hsd_pump file
>>>>>>> d90d1c081e3690e8963e6cd9d05e492656537fd4

echo $nFrames "frames will be used"

#files for GS spectrum
mkdir gs_spectrum
cp dftb_in.hsd_probe gs_spectrum/dftb_in.hsd
cp coords.gen phase_0/charges.bin gs_spectrum

#files for probes
for dir in $pumpdirs; do
cd $dir
mkdir probes

for i in $(seq 0 $nOk); do       #Create probe for each frame
  mkdir probes/frame$i
  cp ../dftb_in.hsd_probe probes/frame$i/dftb_in.hsd
  cp coords.gen charges.bin probes/frame$i
  cp pump_frames/${i}ppdump.bin probes/frame$i/tddump.bin
done

cd ..
done

export OMP_NUM_THREADS=2
echo "Running GS spectrum"
#run GS spectrum
cd gs_spectrum
sed '/[[:blank:]]Probe = Yes/d' ../dftb_in.hsd_probe > dftb_in.hsd
$DFTB_PATH >& out.log
cd ..
echo "Done GS spectrum"

echo "Running probes...."
#run probes
for dir in $pumpdirs; do
echo "Running probes in" $dir
cd $dir/probes
for ff in frame*; do
  cd $ff
  $DFTB_PATH >& out.log &
  cd ..
done
wait
cd ../..
done
