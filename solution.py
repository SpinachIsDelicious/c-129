import pandas as pd

df = pd.read_csv("128.csv")
df.head(10)
df = df.dropna()
df.info()
df.Mass = df.Mass.str.replace("[^a-zA-Z0-9]", "").astype("float")
df["Radius"] = df["Radius"] * (0.102763)
df["Mass"] = df["Mass"] * (0.000954588)
df.to_csv("unit_converted_stars.csv")
import csv
import pandas as pd

file1 = '128.csv'
file2 = '127.csv'

d1 = []
d2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)

    for i in csv_reader:
        d1.append(i)

with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p_d1 = d1[1:]
p_d2 = d2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)