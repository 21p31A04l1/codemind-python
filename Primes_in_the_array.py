def fun(s):
    if s==1:
        return False
    for i in range(2,s):
        if s%i==0:
            return False
    return True
    
n=int(input())
lst=map(int,input().split())
c=0
for i in lst:
    if fun(i):
        c+=1
print(c)