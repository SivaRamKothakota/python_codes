#how many words
n=input()
l=n.split(' ')
j=set(l)
k=0
for i in j:
    k=l.count(i)

    print(i,k,sep="-")

