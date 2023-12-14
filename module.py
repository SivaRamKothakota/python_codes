l=[]
k=[]
n=int(input())
#for i in range(0,n):
#    i=int(input())
 #   l.append(i)
#l=sorted(l)
#print(l)
#l.reverse()
#print(l)

import math
#n=int(input())
k=(1<<int(math.log2(n))+1)-1
print(k)
print(n)

print(n^k)