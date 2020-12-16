""" names.csv
2,nitin
3,rai
45,kwerk
12,udio
32,fast
334,maya
61,turkey
"""

# a) sort the rows of the file by the number field
csv_file = "names.csv"
with open(csv_file, "r") as f:
    lines = sorted(f.readlines(),key=lambda x: int(x.split(",")[0]))
    with open(csv_file, "w") as f:
        f.writelines(lines)

# b) modify the file by removing odd rows (lines number)
with open(csv_file, "r") as f:
    lines = [l for (i,l) in enumerate(f.readlines()) if i%2==0]
    with open(csv_file, "w") as f:
        f.writelines(lines)

# c) store all the names in a string....
with open(csv_file, "r") as f:
    asc = sorted([ord(x) for x in set("".join([x.strip().split(",")[1] for x in f.readlines()]))])
    m_diff = min([asc[i+1] - asc[i]  for i in range(len(asc)-1)])
    print(m_diff)
