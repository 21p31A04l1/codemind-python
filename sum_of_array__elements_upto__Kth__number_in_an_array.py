a=int(input())
lst=list(map(int,input().split()))
x=int(input())
s=0
for i in lst:
    if i==x:
        break
    else:
        s+=i
print(s+x)