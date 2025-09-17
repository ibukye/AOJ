factors=[]
n=int(input())
x=n
i=2
while i*i<=x:
    while x%i==0:factors.append(i);x//=i
    i+=1
if x>1:factors.append(x)
#print(f"{n}: {" ".join(map(str,factors))}")
print(str(n) + ": " + " ".join(map(str, factors)))
