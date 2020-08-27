pdbvol=open("/home/cc59863/SortItOut/A2G_G2S/pdbvol_groupa.txt","r")
pdbvoldict={}
pdbvollst=[]
for line in pdbvol:
	line=line.strip()
	line2=line.split(":")
	key=line2[0]
	#parse resolution
        res=line2[2]
        #apply non membrane multi linear regression
        #linear_vol=float(line2[1])*0.992639271+float(res)*15270.2314-157623.736115305
	linear_vol=float(line2[1])
	#apply linear regression to membrane proteins
	#parse pdb id and volume into a dictionary
	pdbvoldict[key]=linear_vol
	#create a list of volumes
	pdbvollst.append(linear_vol)
print(pdbvoldict)
#sort volume by size
pdbvollst.sort()
#according to sorted volume list, sort pdb id
sortedpdb=[]
for item in pdbvollst:
	for k in pdbvoldict:
		if pdbvoldict[k]==item:
			sortedpdb.append(k)
print(sortedpdb)
pdbvol.close()


emvol=open("/home/cc59863/SortItOut/V2G_G2S/emvol_groupa.txt","r")
emvoldict={}
emvollst=[]
for line in emvol:
        line=line.strip()
	line2=line.split(":")
        key=line2[0]
        #parse emdb id and volume into a dictionary
        emvoldict[key]=float(line2[1])
        #create a list of volumes
        emvollst.append(float(line2[1]))
print(emvoldict)
#sort volume by size
emvollst.sort()
#according to sorted volume list, sort pdb id
sortedem=[]
for item in emvollst:
        for k in emvoldict:
                if emvoldict[k]==item:
			sortedem.append(k)
print(sortedem)
emvol.close()


#sorting
handle= open("fittedpairs_test_3.txt","w")
handle.write("atomid: atom_vol_linear, EMid: EM_vol, diff\n")
print("atomid: atom_vol_linear, EMid: EM_vol, diff")
count=len(sortedem)
for i in range(count):
		pdb=sortedpdb[i]
		emfile=sortedem[i]
		pdb_vol=pdbvoldict[pdb]
		em_vol=emvoldict[emfile]
		print(pdbvoldict[pdb])
		score=abs((pdb_vol-em_vol)/em_vol)
		print(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score))
		handle.write(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score)+"\n")
		#sliding window k=2
		for j in range(2,0,-1):
			if (i-j)>=0:
				emfile=sortedem[i-j]
				pdb_vol=pdbvoldict[pdb]
                        	em_vol=emvoldict[emfile]
                        	score=abs((pdb_vol-em_vol)/em_vol)
				print(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score))
                                handle.write(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score)+"\n")
			if (i+j)<count:
				emfile=sortedem[i+j]
				pdb_vol=pdbvoldict[pdb]
				em_vol=emvoldict[emfile]
				score=abs((pdb_vol-em_vol)/em_vol)
				print(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score))
				handle.write(pdb+": "+str(pdb_vol)+" , "+emfile+": "+str(em_vol)+" , "+str(score)+"\n")
		print("")
		handle.write("\n")
handle.close()
