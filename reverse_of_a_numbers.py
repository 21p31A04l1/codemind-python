n=int(input())
s=0
l=[]
while n:
    l.append(n%10)
    n=n//10
    s=s+1
for i in range(s):
    print(l[i],end="")