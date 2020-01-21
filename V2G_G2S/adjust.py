infile= open("emvol0.txt","r")
outfile= open("emvol_adj.txt","w")
for line in infile:
	line=line.strip()
	content=line.split(":")
	#adjust volume here
	vol=eval(content[1])
	adjvol= (vol-366383.5)/0.99122088
	con= content[0]+" : "+content[1]+" : "+str(adjvol)
	outfile.write(con)
	outfile.write("\n")
infile.close()
outfile.close()
