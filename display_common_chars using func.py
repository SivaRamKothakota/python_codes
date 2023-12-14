def common_chars(*n):
    m=set(n[0])
    k=set()
    for c in n[1:]:
        k=set(c)&m
        print(k)
    print(k)

common_chars("hekko","matoko",'navalo')