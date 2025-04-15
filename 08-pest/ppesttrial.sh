#!/bin/bash
#   script that executes parallel pest
#
DATE=04/12/25
PSLAVES=4 # change this different number of slaves
PPEST=$PEST_DIR/bin/ppest
PSLAVE=$PEST_DIR/bin/pslave
PFLOTRAN=pflotran
CASE=trial # change this for different case name
export PATH=${PATH}:.
if [ -e pslaves.txt ]; then
    rm pslaves.txt #this file keeps track of pslave PIDs
fi
echo "ppestest started at $(date)" > end.txt
I=0
while [ $I -lt $PSLAVES ]; do
 # copy makefile to each pslave subdirectory and run it to copy necessary files
 # into pslave subdirectories
 if [ ! -d pslave$I ]; then 
   mkdir pslave$I
   cp trial.sh pslave$I
   chmod 775 -R pslave$I
   cp PFLOTRAN_pest.py pslave$I
   cp observation.csv pslave$I
   # cp RP_Col3_mZVI_XG.xlsx pslave$I
 fi 
 cd pslave$I
 if [ $? -ne 0 ]; then
        exit 1
 fi

## Start the pslaves
 $PSLAVE < ../run_csh.txt >> out.txt & 
 echo "$!" >> ../pslaves.txt
 cd ../
 I=$[$I+1]
done 
#read -p "press enter"
$PPEST $CASE
echo "ppestest ended at $(date)" >> end.txt
