import numpy as np

l1=[7,8,6,100,7,9]
print(l1)
avg=np.average(l1)
print(avg)
std=np.std(l1)
print(std)
for i in l1:
    z=(i-avg)/std
    print(z)
print("******************************")
x=[85,94,26,46,47,3,5,47,50,43]
mini=min(x)
maxi=max(x)
for i in x:
    l=(i-mini)/(maxi-mini)
    print(i,l)
    