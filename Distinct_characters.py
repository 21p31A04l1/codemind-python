l=input().lower().split()
s=''.join(l)
a='abcdefghijklmnopqrstuvwxyz'
d=[]
for i in a:
    if i in s:
        d.append(i)
for i in d:
    print(i,end="")
