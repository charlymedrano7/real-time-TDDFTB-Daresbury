nphases=4
pi=3.141592653589793

DFTB_PATH=/Users/charly/dftbplus/_build/app/dftb+/dftb+

for i in $(seq 1 $nphases); do
  let ii=$i-1
  phase=$(echo "scale=8; 2*$pi*$ii/$nphases" | bc -l)
  mkdir phase_$ii
  sed "s/         Phase = 0/        Phase = $phase/" dftb_in.hsd_pump > phase_$ii/dftb_in.hsd
  cp coords.gen phase_$ii
done

export OMP_NUM_TREADS=2

for pp in phase_*; do
  cd $pp
  $DFTB_PATH >& out.log &
  cd ..
done
wait
