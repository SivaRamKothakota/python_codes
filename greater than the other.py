n=int(input())
l=[]
k=1
#for i in range(0,n):
    #n=int(input())
    #l.append(n)
#for i in l:
    #if l[0]<i:
       # k=k+1

#print(k)

#product of all digits in a number

j=1
while n!=0:
    d=n%10

    j=j*d
    n=n//10
print(j)
n=input()
p=1
for i in n:
    p*=int(i)
print(p)