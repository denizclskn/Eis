import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Deniz\Documents\Pyth\Grad\virtual\eis\Scripts\eis\main\static\csv\VS30_EXCEL.csv", delimiter=";")

vs30 = np.array(df["VS30"])

for i in range(0, len(vs30)):
    vs30[i] = float(vs30[i])

newvs30 = []   

for i in range(0, len(vs30)):
    newvs30.append(vs30[i])

lat = np.array(df["Enlem"])

for i in range(0, len(lat)):
    lat[i] = float(lat[i])

newLat=[]

for i in range(0, len(lat)):
    newLat.append(lat[i]/10000000)

lng = np.array(df["Boylam"])

for i in range(0, len(lng)):
    lat[i] = float(lng[i])
    
newLng=[]

for i in range(0, len(lng)):
    newLng.append(lng[i]/10000000)

dfp_na = pd.read_csv(r"C:\Users\Deniz\Documents\Pyth\Grad\virtual\eis\Scripts\eis\main\static\csv\parametre.csv",
 delimiter=";")
dfp = dfp_na.dropna()

boy = np.array(dfp["Boylam"])
en = np.array(dfp["Enlem"])
pga10 = np.array(dfp["PGA_10%"])
ss10 = np.array(dfp["SS_10%"])
s1_10 = np.array(dfp["S1_10%"])
pgv10 = np.array(dfp["PGV_10%"])

new_boy = []
new_en = []
new_pga10 = []
new_ss10 = []
new_s1_10 = []
new_pgv10 = []


for i in range(0, len(en)):
    new_boy.append(boy[i])
    new_en.append(en[i])
    new_pga10.append(pga10[i])
    new_ss10.append(ss10[i])
    new_s1_10.append(s1_10[i])
    new_pgv10.append(pgv10[i])
