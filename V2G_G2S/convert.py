infile= open("emoutput.txt","r")
outfile= open("emvol.txt","w")
for line in infile:
	line=line.strip()
	content=line.split()
	if len(content)>=2 and content[0]=="#COMMAND" and content[1]=="./gmconvert":
		file=content[4]
	if len(content)>=1 and content[0]=="#Surface_Model:":
		con= file[:-8]+":"+content[2]
		outfile.write(con)
		outfile.write("\n")
	if len(content)>=1 and content[0]=="error" and content[1]=="flag":
		outfile.write(line)
		outfile.write("\n")
infile.close()
outfile.close()
