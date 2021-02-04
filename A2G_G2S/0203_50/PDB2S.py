import os
import subprocess
import sys
import os.path

infile = open("pdb_nogmm2.txt","r")
for line in infile:
	#parse pdb id from input file
	line = line.strip()
	pdbid = line+".pdb"
	try:
		#download pdb file
		command = "wget https://files.rcsb.org/download/"+pdbid
		subprocess.check_call(command.split())
		command2="scp "+pdbid+" pdbfile0.pdb"
		subprocess.check_call(command2.split())
		command3="chimera --nogui --script surfvol2.py"
		subprocess.check_call(command3.split())
		os.remove(pdbid)
		os.remove("pdbfile0.pdb")
		#os.remove(gmmoutput)
	except:
		print("error")
