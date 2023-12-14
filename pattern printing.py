
n = int(input("Enter the row size:"))


for i in range(n+1):
    for j in range(0,n-i):
        print(" ",end="")

    for p in range(0, i + 1):
        print("*",end=" ")

    #print("\r")
    print("")