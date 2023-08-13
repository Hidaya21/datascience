import math
C=[7,7,3,1]
W=[70,40,40,40]
HA=['Bad','Bad','good','good']
c=int(input("Enter ciegartes: "))
w=int(input("Enter weight: "))
data=[]
for i in range(len(C)):
    x=math.sqrt((c-C[i])**2+(w-W[i])**2)
    data.append(x)
minimum=min(data)
index=data.index(minimum)
print("you belong to ",HA[index])




























