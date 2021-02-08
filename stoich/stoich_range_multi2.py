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
    coefficient=math.trunc(remainder_vol/min_vol)
    lst_res[min_idx]=lst_res[min_idx]+coefficient
    return lst_res

def mincopies(lst_vol,targ_vol):
    lst_res=list(itertools.repeat(1,len(lst_vol)))
    remainder_vol=targ_vol-sum(lst_vol)
    max_vol=max(lst_vol)
    max_idx=lst_vol.index(max_vol)
    coefficient=math.ceil(remainder_vol/max_vol)
    lst_res[max_idx]=lst_res[max_idx]+coefficient
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

def stoich(og_vols,vols,targ,cutoff):
    for i in range(0,len(vols)):
        subunit2(vols,targ,i)
        if i !=0:
            for j in res_list:
                subunit2(list(j),targ,i)

    res_coeff=[]
    for item in res_list:
        if math.ceil(sum(item))>math.trunc(targ)*(1-cutoff) and math.ceil(sum(item))<math.ceil(targ)*(1+cutoff):
            #print(math.ceil(sum(item)))
            res_coeff.append([int(x/y) for x, y in zip(list(item), list(og_vols))])
    print(res_coeff)
        
def recursion_stoich_r(targ,vols,cutoff_st,cutoff_en,increment):
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==1:
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
    else:
        cutoff=cutoff_st
        res_dict={}
        while cutoff <= cutoff_en:
            max_copies2=maxcopies(vols,targ*(1+cutoff))
            max_tot=sum(max_copies2)
            max_num=max(max_copies2)
            min_copies2=mincopies(vols,targ*(1-cutoff))
            min_tot=sum(min_copies2)
            res=[]
            for item in itertools.product(range(1,max_num+1),repeat=len_num):
                item=list(item)
                res_list = []
                if sum(item)<=max_tot: #and sum(item)>=min_tot:
                   for i in range(0, len(item)): 
                       res_list.append(item[i] * vols[i])
                   if sum(res_list)>targ*(1-cutoff) and sum(res_list)<targ*(1+cutoff):
                       res.append(item)
            res_dict[cutoff]=res
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
        while cutoff<=cutoff_en:
            max_copies=maxcopies(vols,targ*(1+cutoff))
            max_num=max(max_copies)
            for item in itertools.product(range(1,max_num),repeat=len_num):
                item=list(item)
                res_list = []
                for i in range(0, len(item)):
                    res_list.append(item[i] * vols[i])
                if sum(res_list)>targ*(1-cutoff) and sum(res_list)<targ*(1+cutoff):
                    res.append(item)
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


infile=open("input4.txt","r")
for line in infile:
    line=line.strip()
    info=line.split(":")
    pdbid=info[0]
    print(pdbid)
    stoich=eval(info[1])
    emvol=float(info[2])
    res=float(info[3])
    vols=eval(info[4])
    targ=(emvol+159785.52734952)/1.14708135
    #targ=(emvol+228522.0665476391-23172.3787*res)/1.07938533
    #targ=(emvol+61363.74335666094-9905.04389*res)/0.988966859
    results=recursion_stoich_r(targ,vols,0.05,2,0.05)
    print(recursion_stoich_tn2(targ,vols,0.05,2,0.05))
    print(find_answers(results,stoich))
    print(print_totalnum(results))
    print("end")
infile.close()
