import os
import subprocess
infile = open("pdb_0826.txt","r")
for line in infile:
	#parse pdb id from input file
	line = line.strip()
	pdbid = line+".pdb"
	try:
		gmmoutput= line+"_50.gmm"
		try:
			#convert pdb to gaussion model then to surface model
			os.system("./A2G_G2S.sh {0} {1}".format(pdbid,gmmoutput))
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
