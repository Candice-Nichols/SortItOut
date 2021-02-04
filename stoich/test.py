infile=open("input.txt","r")
for line in infile:
	line=line.strip()
	info=line.split(":")
	pdbid=info[0]
	print(pdbid)
	string_list=info[1]
	info2=eval(string_list)
	print(type(info2))
	emvol=float(info[2])
	res=float(info[3])
	print(type(res))
	vols=info[4]
	targ=(emvol+61363.74335666094-9905.04389*res)/0.988966859
	
infile.close()
