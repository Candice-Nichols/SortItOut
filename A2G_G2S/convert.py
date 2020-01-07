infile= open("out_100.txt","r")
for line in infile:
	line=line.strip()
	content=line.split()
	if len(content)>=2 and content[0]=="#COMMAND" and content[1]=="./gmconvert":
		file=content[4]
	if len(content)>=1 and content[0]=="#Surface_Model:":
		#print(file[:-8])
		print(content[2])
	if len(content)>=1 and content[0]=="error" and content[1]=="flag":
		print(line)
infile.close()
