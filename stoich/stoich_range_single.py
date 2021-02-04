import math
import itertools
import  itertools
#assuming 3 subunits, subunit A,B,C
#Vol (A) =3, Vol (B)=4, Vol(C)=5
#maximum copies of subunits for total volume y would be 
#[1,1,1] (each subunit must be present at least once) 
# plus
#[(y-3-4-5)/3,0,0] (remainder of volume / the smallest subunit)
def maxcopies(lst_vol,targ_vol):
    lst_res=list(itertools.repeat(1,len(lst_vol)))
    remainder_vol=targ_vol-sum(lst_vol)
    min_vol=min(lst_vol)
    min_idx=lst_vol.index(min_vol)
    coefficient=int(remainder_vol//min_vol+1)
    lst_res[min_idx]=lst_res[min_idx]+coefficient
    return lst_res

def subunit2(vols,target,p):
    res_list=[og_vols]
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

def recursion_stoich_r(targ,vols,cutoff_st,cutoff_en,increment):
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==0:
        return
    else:
        cutoff=cutoff_st
        res_dict={}
        while cutoff <= cutoff_en:
            res=[]
            print(cutoff)
            max_num=math.ceil(targ*(1+cutoff)/vols[0])
            for item in itertools.product(range(1,max_num),repeat=len_num):
                item=list(item)
                res_list = []
                for i in range(0, len(item)): 
                    res_list.append(item[i] * vols[i])
                if sum(res_list)>targ*(1-cutoff) and sum(res_list)<targ*(1+cutoff):
                    res.append(item)
            res_dict[cutoff]=res
            cutoff+=increment
        return res_dict

def recursion_stoich_tn(targ,vols,cutoff_st,cutoff_en,increment):
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==0:
        return
    else:
        cutoff=cutoff_st
        res_dict={}
        while cutoff <= cutoff_en:
            res=[]
            tn_count=0
            max_num=math.ceil(targ*(1+cutoff)/vols[0])
            for item in itertools.product(range(1,max_num),repeat=len_num):
                item=list(item)
                res_list = []
                for i in range(0, len(item)): 
                    res_list.append(item[i] * vols[i])
                if sum(res_list)>targ*(1-cutoff) and sum(res_list)<targ*(1+cutoff):
                    res.append(item)
                else:
                    tn_count+=1
            res_dict[cutoff]=tn_count
            cutoff+=increment
        return res_dict

def recursion_stoich_tn2(targ,vols,cutoff_st,cutoff_en,increment):
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==0:
        return
    else:
        cutoff=cutoff_st
        res_dict={}
        res=[]
        tn_count=0
        max_num=math.ceil(targ*(1+cutoff)/vols[0])
        for item in itertools.product(range(1,max_num),repeat=len_num):
            item=list(item)
            res_list = []
            for i in range(0, len(item)): 
                res_list.append(item[i] * vols[i])
            if sum(res_list)>targ*(1-cutoff) and sum(res_list)<targ*(1+cutoff):
                res.append(item)
            else:
                tn_count+=1
        res_dict[cutoff]=tn_count
        cutoff+=increment
    return res_dict
    
def find_answers(dic,ans):
    for item in dic.keys():
        lst=dic[item]
        l=len(lst)
        if ans in lst:
            print(str(item) +" TRUE "+str(l))
            break
        else:
            print(str(item) +" FALSE "+str(l))

def print_totalnum(dic):
    for item in dic.keys():
        lst=dic[item]
        l=len(lst)
        print(str(l))


infile=open("input3.txt","r")
for line in infile:
    line=line.strip()
    info=line.split(":")
    pdbid=info[0]
    print(pdbid)
    stoich=tuple(eval(info[1]))
    emvol=float(info[2])
    res=eval(info[3])
    vols=eval(info[4])
    ogvols=tuple(eval(info[4]))
    targ=(emvol+121000.18327867)/1.0922644
    #targ=(emvol+228522.0665476391-23172.3787*res)/1.07938533
    #targ=(emvol+61363.74335666094-9905.04389*res)/0.988966859
    results=recursion_stoich_r(targ,vols,0.05,2,0.05)
    print(recursion_stoich_tn2(targ,vols,0.05,2,0.05))
    print(find_answers(results,eval(info[1])))
    print(print_totalnum(results))
    print("end")
infile.close()

