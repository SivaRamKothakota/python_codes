#capital ,small,numbers
n=input("write=")
class happy():

     print({i for i in n if i.isdigit()},{k for k in n if k.isupper()},{j for j in n if j.islower()},sep="  --   ")

