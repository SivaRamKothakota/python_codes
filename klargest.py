n=int(input())
k=int(input())
m=-k-1
import numpy as np
j=[]
for i in range(0,n):
    n=int(input())
    j.append(n)
j=sorted(j)
for i in j[-1:m:-1]:
    print(i)


