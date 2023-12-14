
k=[]
n=[]
while True:
    o=input()
    p=input()
    if o=='end':
        break
    else:
        n.append(o)
        k.append(p)
for i,l in enumerate(n):
        if i>=len(k):
            k1='unknow'

        else:
            k1=k[i]
        print(l,k1)
