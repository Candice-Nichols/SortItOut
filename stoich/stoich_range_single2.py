infile=open("input3.txt","r")
def subunit2(vols,target,p):
    s = sum(vols)
    if s>target*1.2:
        return
    if s<target*1.2:
        vols[p]= vols[p]+og_vols[p]
        #print(vols)
        #print(vols)
        if tuple(vols) not in res_list:
            res_list.append(tuple(vols))
        subunit2(vols,target,p)
for line in infile:
    line=line.strip()
    info=line.split(":")
    pdb_id=info[0]
    og_vols=tuple(eval(info[4]))
    targ=(float(info[2])+121000.18327867)/1.0922644
    print(targ)
    print(og_vols)
    res_list=[og_vols]
    for i in range(0,len(vols)):
        subunit2(vols,targ,i)
        if i !=0:
            for j in res_list:
                subunit2(list(j),targ,i)
    res_coeff=[]
for item in r
