import os
import subprocess
infile = open("test_input2.txt","r")
for line in infile:
	#parse emd id from input file
	line = line.strip()
	content=line.split(":")
	emdb = content[0]
	emdbid = emdb[4:]
	emfile = "emd_"+emdbid+ ".map"
	#parse contour lvl
	contour= float(content[1])
	try:
		#download emdb file and unzip file
		command = "wget ftp://ftp.wwpdb.org/pub/emdb/structures/EMD-"+emdbid+"/map/emd_"+emdbid+".map.gz"
		command2 = "gunzip "+emfile+".gz"
		subprocess.check_call(command.split())
		subprocess.check_call(command2.split())
		gmmoutput= "emd_"+emdbid+"_100.gmm"
		try:
			#convert em map to gaussion model, then to surface model
			os.system("./V2G_G2S.sh {0} {1} {2}".format(emfile,gmmoutput,contour))
			os.remove(emfile)
			os.remove("pdbfile.pdb")
			os.remove(gmmoutput)
		except:
			#raise error if fail to convert em map
			print("error flag: fail to convert")
	except:
		#raise error if em file cannot be found
		print("error flag: emdb not found")
