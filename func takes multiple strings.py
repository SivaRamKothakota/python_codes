
def strings(*n):
    chars=set()
    for c in n:
        c=set(c)
        chars=c.union(chars)
    print(chars)
strings('hello', 'hi', 'hey', 'noo')
