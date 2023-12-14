n = int(input(''))
for m in range(1, n // 2 + 1):
    if n % m == 0:
        print(m,end=',')
        m += 1
print(n,end="")