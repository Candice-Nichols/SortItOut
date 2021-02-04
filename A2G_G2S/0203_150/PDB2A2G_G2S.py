import os
import subprocess
infile = open("input.txt","r")
for line in infile:
	#parse pdb id from input file
	line = line.strip()
	pdbid = line+".pdb"
	try:
		#download pdb file
		command = "wget https://files.rcsb.org/download/"+pdbid
		subprocess.check_call(command.split())
		gmmoutput= line+"_150.gmm"
		try:
			#convert pdb to gaussion model then to surface model
			os.system("./A2G_G2S.sh {0} {1}".format(pdbid,gmmoutput))
			os.remove(pdbid)
			os.remove("pdbfile0.pdb")
			os.remove(gmmoutput)
		except:
			#raise error if program fail to convert pdb
			f="error flag: fail to convert"+gmmoutput
			print(f)
	except:
		#raise error if program fail to download pdb file
		t="error flag: pdb not found" + line
		print(t)
