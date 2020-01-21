#!/bin/bash
#download and calculate pdb volume
#echo "start pdb calculation"
#cd A2G_G2S
#nohup python PDB2A2G_G2S.py > pdboutput.txt
#python convert.py
#cd ..

#download and calculate em volume
echo "start em calculation"
cd V2G_G2S
nohup python EMDB2V2G_G2S.py > emoutput.txt
python convert.py
cd ..
