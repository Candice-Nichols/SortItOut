input="$1"

outputgmm="$2"
outputpdb="pdbfile.pdb"

#convert atomic structure to gaussion
./gmconvert V2G -imap $input -ogmm $2 -ng 100 -max_memory 16000

#convert gaussion to surface
./gmconvert G2S -igmm $2 -gw 4 -opdb pdbfile.pdb -max_memory 16000

#calculate surface volume using chimera
chimera --nogui --script surfacevol.py
