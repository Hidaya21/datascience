o=[7,5,2,0,1,8]
F=[6,5,0,-1,0,7]
sum=0
for i in range(len(o)):
    sum=sum+(F[i]-o[i])**2
MSE=sum/len(o)
print(MSE)








