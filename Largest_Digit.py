n=int(input())
l=[]
k=0
while n:
    l.append(n%10)
    n=n//10
    k=k+1
l.sort()
print(l[k-1])
