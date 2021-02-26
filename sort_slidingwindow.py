pdbvol=open("/home/cc59863/SortItOut/A2G_G2S/pdbvol_overall2.txt","r")
pdbvoldict={}
pdbvollst=[]
for line in pdbvol:
    line=line.strip()
    line2=line.split(":")
    key=line2[0]
    res=line2[2]
    #apply lr new
    #linear_vol=float(line2[1])*1.07938533+23172.3787*float(res)-228522.066547639
    #apply lr new 0204
    #linear_vol=float(line2[1])*1.14708135-159785.52734952
    #apply lr new 0219
    linear_vol=float(line2[1])*0.91657308-51187.65809547
    #apply linear regression to membrane proteins
    #linear_vol=float(line2[1])*0.658359617+23528.3482*float(res)-30957.365008784633
    #linear_vol=float(line2[1])
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


emvol=open("/home/cc59863/SortItOut/V2G_G2S/emvol_overall2.txt","r")
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
    #sliding window k=3
    for j in range(3,0,-1):
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
