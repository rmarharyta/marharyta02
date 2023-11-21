#20 варіант, друге завдання
import pandas as pd 
import math

f=open("cords.txt",'r') 
x1=[] 
y1=[] 
list=[]
for lines in f:
    x=lines.index(' ') 
    s1=lines[0:x] 
    s2=lines[(x+1):-1] 
    x1.append(float(s1)) 
    y1.append(float(s2))
f.close() 

def distance(point1, point2):
    return round(math.sqrt(math.pow((point2[0] - point1[0]),2) + math.pow((point2[1] - point1[1]),2)),2)

side1 = distance((x1[0], y1[0]), (x1[1], y1[1]))
side2 = distance((x1[1], y1[1]), (x1[2], y1[2]))
side3 = distance((x1[2], y1[2]), (x1[3], y1[3]))
side4 = distance((x1[3], y1[3]), (x1[0], y1[0]))

m=pd.Series([side1,side2,side3,side4],["side1","side2","side3","side4"])

diagonal1=distance((x1[0], y1[0]), (x1[2], y1[2]))
diagonal2=distance((x1[1], y1[1]), (x1[3], y1[3]))

m["diagonal1"] = diagonal1
m["diagonal2"] = diagonal2
m.to_json("figure.json",orient='index')