num = int(input("num="))
z = 0
for n in range(1, num // 2 + 1):
    if num % n == 0:
        z = z + n
if z == num:
    print("perfect number ")
else:
    print("not")
