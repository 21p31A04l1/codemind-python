n,m=map(int,input().split())
l=[]
a=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(m):
    s=0
    for j in range(n):
        s=s+l[j][i]
    a.append(s)
print(max(a))
    