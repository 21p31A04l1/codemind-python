n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
a=l.index(min(l))
b=l.index(max(l))
for i in range(0,n):
    f=0
    for j in range(2,l[i]):
        if l[i]%j==0:
            f=f+1
    if l[i]>1 and l[i]!=0 and f==0:
        s1=s1+1
        s2=s2+l[i]
print('{:.2f}'.format(s2/s1))