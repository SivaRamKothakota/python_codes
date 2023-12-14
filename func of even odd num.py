n = (1, 2,7, 3,  5, 6, 8, 9,4)

o=[]
l=[]
for k in filter(lambda k : k % 2 == 1,n):
    l.append(k)
for j in filter(lambda j: j%2==0,n):
    o.append(j)
print(f"even={sorted(l)}\nodd={sorted(o)}")
#for d in sorted(n,key=lambda d:d%2==1):

    #l.append(d)
#print(l)
#print(sorted ( n,key=lambda v:v%2==1))
