#same characters in both strings
n = input('first string is:')
b = input("second string")
k=set(n)
l=set(b)
if min(k,l)<max(k,l):
    print('yes')
else:
    print("no")