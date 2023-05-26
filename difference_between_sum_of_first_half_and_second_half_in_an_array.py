n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
c=n//2
for i in lst:
    if i>c:
        a.append(i)
    else:
        b.append(i)
print(sum(a)-sum(b))