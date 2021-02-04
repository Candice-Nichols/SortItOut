import os
import subprocess
infile = open("0203_input.txt","r")
for line in infile:
	#parse emd id from input file
	line = line.strip()
	emdbid = line[4:]
	emfile = "emd_"+line[4:] + ".map"
	try:
		#download emdb file and unzip file
		command = "wget ftp://ftp.wwpdb.org/pub/emdb/structures/EMD-"+emdbid+"/map/emd_"+emdbid+".map.gz"
		command2 = "gunzip "+emfile+".gz"
		command3 = "wget https://www.ebi.ac.uk/pdbe/entry/download/EMD-"+emdbid+"/xml"
		subprocess.check_call(command.split())
		subprocess.check_call(command2.split())
		subprocess.check_call(command3.split())
		gmmoutput= "emd_"+line[4:]+"_100.gmm"
		infileinfo=open("xml","r")
		for line in infileinfo:
			line=line.strip()
			if line[:13]=="<contourLevel":
                                content=line.split(">")
                                content2=content[1].split("<")
                                contour=content2[0]
                                print(content2[0])

		try:
			#convert em map to gaussion model, then to surface model
			os.system("./V2G_G2S.sh {0} {1} {2}".format(emfile,gmmoutput,contour))
			os.remove(emfile)
			os.remove("pdbfile.pdb")
			os.remove(gmmoutput)
			os.remove("xml")
		except:
			#raise error if fail to convert em map
			print("error flag: fail to convert")
	except:
		#raise error if em file cannot be found
		print("error flag: emdb not found")
