pdbvol=open("/home/cc59863/SortItOut/A2G_G2S/pdbvol_test.txt","r")
pdbvoldict={}
pdbvollst=[]
for line in pdbvol:
	line=line.strip()
	line2=line.split(":")
	key=line2[0]
	linear_vol= float(line2[1])*0.99122088+36683.5
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


emvol=open("/home/cc59863/SortItOut/V2G_G2S/emvol_test.txt","r")
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
	score_dict={}
	lst_score=[]
	pdb_vol=float(pdbvoldict[pdb])
	em_vol=float(emvoldict[emfile])
	score=abs((pdb_vol-em_vol)/em_vol)
	lst_score.append(score)
        setpair = (pdb,emfile,0)
        score_dict[setpair]=score

	#nearest neighbor k=2
	for j in range(2,0,-1):
		if (i-j)>=0:
			emfile=sortedem[i-j]
			pdb_vol=float(pdbvoldict[pdb])
                       	em_vol=float(emvoldict[emfile])
                       	score=abs((pdb_vol-em_vol)/em_vol)
			lst_score.append(score)
                        setpair = (pdb,emfile,-j)
                        score_dict[setpair]=score
		if (i+j)<count:
			emfile=sortedem[i+j]
			pdb_vol=float(pdbvoldict[pdb])
			em_vol=float(emvoldict[emfile])
			score=abs((pdb_vol-em_vol)/em_vol)
			lst_score.append(score)
                        setpair = (pdb,emfile,j)
                        score_dict[setpair]=score
	lst_score.sort()
        min_diff = lst_score[0]
        for k in score_dict:
                if min_diff == score_dict[k]:
                        x,y,z=(k)
			print()
	lst_index= [z-2,z-1,z,z+1,z+2]
        for index in lst_index:
                index2= i+index
                if index2>=0 and index2<count:
                        #print(index)
                        emfile_2 = sortedem[index2]
                        emvol2=float(emvoldict[emfile_2])
                        score=abs((pdb_vol-emvol2)/emvol2)
                        print(pdb+": "+str(pdb_vol)+" , "+emfile_2+" , "+str(emvol2)+" , "+str(score))
                if index2<0:
                        index2= i-index+2
                        #print(index2)
			emfile_2=sortedem[index2]
                        emvol2= float(emvoldict[emfile_2])
                        score=abs((pdb_vol-emvol2)/emvol2)
                        print(pdb+": "+str(pdb_vol)+" , "+emfile_2+" , "+str(emvol2)+" , "+str(score))
                if index2>=count:
			index2 = i-index-2
                        #print(index2)
                        emfile_2 = sorted_em[index2]
			emvol2= float(emvoldict[emfile_2])
                        score=abs((pdb_vol-emvol2)/emvol2)
                        print(pdb+": "+str(pdb_vol)+" , "+emfile2+" , "+str(emvol2)+" , "+str(score))
print()

handle.close()
