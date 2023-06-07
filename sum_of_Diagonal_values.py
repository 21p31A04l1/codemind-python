n,m=map(int,input().split())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
s=0
for i in range(n):
    for j in range(m):
        if i==j or j==m-i-1:
            s=s+l[i][j]
print(s)