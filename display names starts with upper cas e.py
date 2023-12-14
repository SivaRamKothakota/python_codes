def upper_lower(*n):
    l=[]
    for c in n[::]:
        if c[0].isupper() and c[-1].islower():
            l.append(c)


    print(l)


upper_lower("names","Names","Kota","ram",'Ram')
