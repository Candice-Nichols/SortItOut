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
### For EM volume calculation using manually entered countour level, format input as following
```
EMDB_3488:4.0
...
```
### Run program
```
nohup python EMDB2V2G_G2S2.py > gmm_output.txt &
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

## subunit volume calculation

### Navigate to corresponding directory
```
cd subunit_vol
```
### Create input file "subunit_input.txt", and edit with PDB ids and chain, format as following
```
6e14 H
6e14 D
...
```
### Run program. (Resulting pdb files will be written in results folder)
```
python subunit.py
```
