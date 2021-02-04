import os
import subprocess
infile = open("input3.txt","r")
for line in infile:
	#parse pdb id from input file
	line = line.strip()
	content=line.split()
	pdbid = content[0]+"_chain"+content[1]+".pdb"
	try:
		gmmoutput= content[0]+"_chain"+content[1]+"_50.gmm"
		try:
			#convert pdb to gaussion model then to surface model
			os.system("./A2G_G2S.sh {0} {1}".format(pdbid,gmmoutput))
			#os.remove(pdbid)
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
