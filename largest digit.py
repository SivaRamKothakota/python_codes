def largest_digit(n):
    j=0
    k=0
    while n>0:
        j=n%10
        n=n//10
        if j>k:


            k=j
    return(k)
print(largest_digit(87923))

