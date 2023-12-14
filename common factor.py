n, m = int(input('the first  number given is:')), int(input('the second number given is: '))
small_number=min(n,m)
for l in range(1, small_number + 1):
    if n % l == 0 and n % l == m % l:
        k = l
        print(k)

