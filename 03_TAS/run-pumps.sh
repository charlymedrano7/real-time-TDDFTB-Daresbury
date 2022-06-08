nphases=4                  #Number of phases
pi=3.141592653589793       #Needed for the phases

DFTB_PATH=/mnt/ceph/course_materials/opt/dftbplus-main/bin/dftb+

for i in $(seq 1 $nphases); do         #Create a folder for each phase       
  let ii=$i-1
  phase=$(echo "scale=8; 2*$pi*$ii/$nphases" | bc -l)
  mkdir phase_$ii
  sed "s/         Phase = 0/        Phase = $phase/" dftb_in.hsd_pump > phase_$ii/dftb_in.hsd
  cp coords.gen phase_$ii
done

export OMP_NUM_TREADS=2

for pp in phase_*; do                  #Run the pump in each phase
  cd $pp
  $DFTB_PATH >& out.log &
  cd ..
done
wait
