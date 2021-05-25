#!/bin/bash
###################################################################################
# Omar Hernández Montes		24 MAY 2021
# With this script plus 'denchar_2D.py' program you will get 2D plot for Denchar
# Change 'label' var for the label name of your structure according to SIESTA syntaxis: label.CON.SCF
# Ensure this script has all the permissions to be executed
# If you want additional features on your plot edit 'denchar_2D.py' program
###################################################################################
FILE=label
awk '{print $1,$2,$3}' $FILE.CON.SCF >> "$FILE"_dummy_scf
grep -i "\S" "$FILE"_dummy_scf >> "$FILE"_denchar.scf
sed -i 's/ /,/g' "$FILE"_denchar.scf
rm "$FILE"_dummy_scf
wc -l "$FILE"_denchar.scf | awk '{print $1}' > Np
let NP=`cat Np`
sed -i 's/NPOINTS/'$NP'/g' denchar_2D.py
sed -i 's/filename/'$FILE'/g' denchar_2D.py
#If you want to save the plot in a .png file uncomment the next line:
#sed -i 's/#plt.savefig/plt.savefig/g' denchar_2D.py
python3 denchar_2D.py
sed -i 's/'$FILE'/filename/g' denchar_2D.py
sed -i 's/'$NP'/NPOINTS/g' denchar_2D.py
rm "$FILE"_denchar.scf
rm Np
