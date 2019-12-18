import os
import subprocess
infile = open("gmminput.txt","r")
for line in infile:
	line = line.strip()
	pdbid = line+".pdb"
	try:
		command = "wget https://files.rcsb.org/download/"+pdbid
		subprocess.check_call(command.split())
		gmmoutput= line+"_100.gmm"
		try:
			os.system("./A2G_G2S.sh {0} {1}".format(pdbid,gmmoutput))
			os.remove(pdbid)
			os.remove("pdbfile0.pdb")
			os.remove(gmmoutput)
		except:
			f="error flag: fail to convert"+gmmoutput
			print(f)
	except:
		t="error flag: pdb not found" + line
		print(t)
