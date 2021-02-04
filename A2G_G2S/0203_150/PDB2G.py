import os
import subprocess
infile = open("pdb_0605.txt","r")
for line in infile:
        #parse pdb id from input file
        line = line.strip()
        pdbid = line+".pdb"
        try:
	#download pdb file
                command = "wget https://files.rcsb.org/download/"+pdbid
                subprocess.check_call(command.split())
                gmmoutput= line+"_100.gmm"
		finalout= line+"_100.pdb"
                try:
                        #convert pdb to gaussion model then to surface model
                        os.system("./gmconvert A2G -ipdb {0} -ng 100".format(pdbid))
			os.system("./gmconvert G2S -igmm {0} -gw 4 -opdb {1}".format(gmmoutput,finalout))
		except:
			next
	except:
		next
