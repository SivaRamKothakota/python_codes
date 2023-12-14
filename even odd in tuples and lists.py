n=int(input('how many numbers:'))
l=[]
for i in range (1,n+1):
    k=int(input('user given'))
    if k%2!=0:
        l.append(k)
    else:
        l.insert(0,k)

print(l)