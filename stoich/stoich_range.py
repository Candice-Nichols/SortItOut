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

def stoich(og_vols,vols,targ,cutoff):
    for i in range(0,len(vols)):
        subunit2(vols,targ,i)
        if i !=0:
            for j in res_list:
                subunit2(list(j),targ,i)

    res_coeff=[]
    for item in res_list:
        if math.ceil(sum(item))>math.ceil(targ)*(1-cutoff) and math.ceil(sum(item))<math.ceil(targ)*(1+cutoff):
            #print(math.ceil(sum(item)))
            res_coeff.append([int(x/y) for x, y in zip(list(item), list(og_vols))])
    print(res_coeff)
        
def recursion_stoich_r(targ,vols,cutoff_st,cutoff_en,increment):
    max_copies=maxcopies(vols,targ*(1+cutoff_en))
    max_num=max(max_copies)
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==1:
        stoich(og_vols,vols,targ,cutoff_st)
    else:
        cutoff=cutoff_st
        res_dict={}
        while cutoff <= cutoff_en:
            res=[]
            print(cutoff)
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
    max_copies=maxcopies(vols,targ*(1+cutoff_en))
    max_num=max(max_copies)
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==1:
        stoich(og_vols,vols,targ,cutoff_st)
    else:
        cutoff=cutoff_st
        res_dict={}
        while cutoff <= cutoff_en:
            res=[]
            tn_count=0
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
    max_copies=maxcopies(vols,targ*(1+cutoff_en))
    max_num=max(max_copies)
    len_num=len(vols)
    og_vols=tuple(vols)
    if len_num==1:
        stoich(og_vols,vols,targ,cutoff_st)
    else:
        cutoff=cutoff_st
        res_dict={}
        res=[]
        tn_count=0
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


print("4ci0")
vols=[41472.63,22725.11,28609.86]
targ=(1064768-4810.83316*3.36)/0.988867489
res=recursion_stoich_r(targ,vols,0.01,1,0.01)
print(recursion_stoich_tn2(targ,vols,0.01,1,0.01))
print(find_answers(res,[12,12,12]))
print(print_totalnum(res))
print("end")
print("4atx")
vols=[48202.23,48168.27,33592.58]
targ=(3236346.25-4810.83316*8.2)/0.988867489
res=recursion_stoich_r(targ,vols,0.01,1,0.01)
print(recursion_stoich_tn2(targ,vols,0.01,1,0.01))
print(find_answers(res,[14,14,14]))
print(print_totalnum(res))
print("end")
print("3iz0")
vols=[28375.63,19718.28,46533.23,48157.36]
targ=(10805728-4810.83316*8.6)/0.988867489
res=recursion_stoich_r(targ,vols,0.01,1,0.01)
print(recursion_stoich_tn2(targ,vols,0.01,1,0.01))
print(find_answers(res,[78,78,39,39]))
print(print_totalnum(res))
print("end")
print("3j8x")
vols=[50407.55,50289.04,33718.65]
targ=(5852245-4810.83316*5)/0.988867489
res=recursion_stoich_r(targ,vols,0.01,1,0.01)
print(recursion_stoich_tn2(targ,vols,0.01,1,0.01))
print(find_answers(res,[42,42,42]))
print(print_totalnum(res))
print("end")
