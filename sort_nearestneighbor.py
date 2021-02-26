import numpy as np
import scipy
pdbvol=open("/home/cc59863/SortItOut/A2G_G2S/pdbvol_overall.txt","r")
pdbvoldict={}
pdbvollst=[]
pdbarr=[]
for line in pdbvol:
        line=line.strip()
        line2=line.split(":")
        key=line2[0]
	#parse resolution
        res=line2[2]
        #apply lr new
        #linear_vol=float(line2[1])*1.07938533+23172.3787*float(res)-228522.066547639
        #apply new lr 0204
        #linear_vol=float(line2[1])*1.14708135-159785.52734952
        #apply new lr 0219
        linear_vol=float(line2[1])*0.91657308-51187.65809547
        #apply linear regression for membrane proteins
        #linear_vol= float(line2[1])*0.658359617+23528.3482*float(res)-30957.365008784633
        #linear_vol=float(line2[1])
	#parse pdb id and volume into a dictionary
        pdbvoldict[key]=linear_vol
        #create a list of volumes
        pdbvollst.append(linear_vol)
#print(pdbvoldict)
#sort volume by size
pdbvollst.sort()
#according to sorted volume list, sort pdb id
sortedpdb=[]
count=0
for item in pdbvollst:
	for k in pdbvoldict:
		if pdbvoldict[k]==item:
			sortedpdb.append(k)
			pdbarr.append([float(0),float(item)])
			count+=1
#print(sortedpdb)
#print(pdbarr)
pdbvol.close()

emvol=open("/home/cc59863/SortItOut/V2G_G2S/emvol_overall.txt","r")
emvoldict={}
emvollst=[]
emarr=[]
for line in emvol:
        line=line.strip()
        line2=line.split(":")
        key=line2[0]
        #parse emdb id and volume into a dictionary
        emvoldict[key]=float(line2[1])
        #create a list of volumes
        emvollst.append(float(line2[1]))
#print(emvoldict)
#sort volume by size
emvollst.sort()
#according to sorted volume list, sort pdb id
sortedem=[]
#for item in emvollst:
count=0
for item in emvollst:
	for k in emvoldict:
		if emvoldict[k]==item:
			sortedem.append(k)
			emarr.append([float(0),float(item)])
			count+=1
#print(sortedem)
#print(emarr)
emvol.close()

from scipy.spatial import distance
#transform data to array
pdb_array=np.array(pdbarr)
em_array=np.array(emarr)

#to find emdb id or pdb id it's sortedem(pdb(i)) or sortedpdb(em(i))
res=distance.cdist(pdb_array,em_array)

#print(distance.cdist(pdb_array,em_array))
print()
#print(np.array2string(res,formatter={'float_kind':'{0:.1f}'.format}))

print(res)
for i in range (len(res)):
	pdbfile=sortedpdb[i]
	print(pdbfile+" : "+str(pdbvoldict[pdbfile]))
	ilst=list(res[i])
	plst=list(res[i])
	plst.sort()
	#find smallest 2 distances
	for j in range (0,2):
		dist_diff=plst[j]
		idx=ilst.index(dist_diff)
		idxem=sortedem[idx]
		emvol=emvoldict[idxem]
		print(str(idxem)+" : "+str(emvol)+", diff= "+str(dist_diff))
	print("")
	#print(ilst)
	#print(plst)
