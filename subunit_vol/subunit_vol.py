from biopandas.pdb import PandasPdb
infile=open("subunit_input.txt","r")
for line in infile:
	line=line.strip()
	content=line.split()
	pdbid=content[0]
	chain=content[1]
	output="results/"+pdbid+"_chain"+chain+".pdb"
	ppdb = PandasPdb().fetch_pdb(pdbid)
	ppdb.df['ATOM'] = ppdb.df['ATOM'][ppdb.df['ATOM']['chain_id'] == chain]
	ppdb.to_pdb(path=output,records=None,gz=False,append_newline=True)
