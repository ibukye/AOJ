"""
factors=[]
n=int(input())
x=n
i=2
while i<n:
    if x%i==0:factors.append(i);x//=i
    i+=1
if x>1:factors.append(x)
print(n-len(factors))
"""