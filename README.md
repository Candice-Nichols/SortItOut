# SortItOut
Matching atomic protein subunit structure into protein complex EM maps



## V2G_G2S Calculation

### Navigate to corresponding directory
```
cd V2G_G2S
```

### Create input file "gmm_input.txt", and edit with EMDB ids, format as following
```
EMDB_3488
EMDB_3204
...
```

### Run program
```
nohup python EMDB2V2G_G2S.py > gmm_output.txt &
```

### to edit Ngauss edit in V2G_G2S.sh
```
./gmconvert V2G -imap $input -ogmm $2 -ng 100 -zth $contour -max_memory 90000
```



## A2G_G2S Calculation

### Navigate to corresponding directory
```
cd A2G_G2S
```

### Create input file "gmm_input.txt", and edit with PDB ids, format as following
```
5jwl
3b8k
...
```

### Run program
```
nohup python PDBA2G_G2S.py > gmm_output.txt &
```
### to edit Ngauss edit in A2G_G2S.sh
```
./gmconvert A2G -ipdb $input -ng 100
```

