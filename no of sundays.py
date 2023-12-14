n=input()
m=0
s=0
t=int(input())
if n=='mon':
    m=1
if n=='tue':
    m=2
if n=="fri":
    m=5
k=7-m
h=t-k

if h>=0:
    s=h//7+1
    print(s)
else:
    print('zero')