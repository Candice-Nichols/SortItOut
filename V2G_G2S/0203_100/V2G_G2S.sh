input="$1"

outputgmm="$2"
contour="$3"
outputpdb="pdbfile.pdb"

#convert atomic structure to gaussion
./gmconvert V2G -imap $input -ogmm $2 -ng 100 -zth $contour -max_memory 90000

#convert gaussion to surface
./gmconvert G2S -igmm $2 -gw 4 -opdb pdbfile.pdb -max_memory 90000

#calculate surface volume using chimera
#chimera --nogui --script surfacevol.py
