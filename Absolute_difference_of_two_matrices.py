n=int(input())
m1=[list(map(int,input().split())) for i in range(n)]
m2=[list(map(int,input().split())) for i in range(n)]
l=[]
for i in range(n):
    a = []
    for j in range(n):
        m1[i][j] = abs(m1[i][j]-m2[i][j])
        a.append(m1[i][j])
    l.append(a)
for i in l:
    print(*i)