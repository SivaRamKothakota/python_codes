num = int(input("num="))
m = 0
for n in range( num // 2 + 1,0,-1):
    if num % n == 0:
        print(n)
        break
