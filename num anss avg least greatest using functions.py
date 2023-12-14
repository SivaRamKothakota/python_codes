def numbers(*n):
    count = 0
    least = 0
    greatest = 0
    r = 0

    for c in n:

        count = count + c

        r += 1
        if least == 0:
            least = c
        elif least > c:
            least = c
        if greatest==0:
            greatest=c
        if greatest < c:
            greatest = c

    avg = count // r

    print(f"count={count},avg={avg},least={least},greatest={greatest}")


numbers(-10,- 20,- 30, -40,-1, -90, -100)
