st = "how do you do today?"

chars = {'o':1}
for c in st:
    count = chars.get(c, 0)
    print(count)
    chars[c] = count + 1
    print(chars[c],chars)
#for k,v in chars.items():

   #  if v==1:
       # print(k)

#print(chars)