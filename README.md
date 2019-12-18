# SortItOut
Matching atomic protein subunit structure into protein complex EM maps



## V2G_G2S Calculation

### Navigate to corresponding directory
```
cd V2G_G2S
```

### Create input file "gmminput.txt", and edit with EMDB ids, format as following
```
EMDB_3488
EMDB_3204
...
```

### Run program
```
python EMDBV2G_G2S.py
```




## A2G_G2S Calculation

### Navigate to corresponding directory
```
cd A2G_G2S
```

### Create input file "gmminput.txt", and edit with PDB ids, format as following
```
5jwl
3b8k
...
```

### Run program
```
python PDBA2G_G2S.py
```
