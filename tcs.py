n=input()
s=0
l=0
k=0
h=0
m=0
for i in n:
    if n.count(i)==1:
        s=s+1
    if n.count(i)>1:
        if n.count(i)<=2:
            l=l+1

    if n.count(i)>2:
        k=k+1

        m=n.count(i)
        h=k//m
h=h+l//2
print(h)
print(s)
#if k==m and l==0:
   # print('proceed')
#if k==0 and l//2==1:
 #   print('proced')
if s>1 and h>1:
    print('stop')
elif s<1 and h>1:
    print("f")
else :
    print("p")
#if s==1 and l//2>1 and k==0:
   # print('proceed')
#if s==1 and l//2==0 and k!=m:
  #  print( 'proceed')

