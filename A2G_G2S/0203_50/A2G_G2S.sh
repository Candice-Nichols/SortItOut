input="$1"

outputgmm="$2"
outputpdb="pdbfile0.pdb"

#convert atomic structure to gaussion
./gmconvert A2G -ipdb $input -ng 50

#convert gaussion to surface
./gmconvert G2S -igmm $2 -gw 4 -opdb pdbfile0.pdb

#calculate surface volume using chimera
#chimera --nogui --script surfacevol.py
