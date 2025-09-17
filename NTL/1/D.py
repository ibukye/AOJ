import math
n=int(input())
cnt=0
for i in range(1,n):
    if math.gcd(n,i)==1:cnt+=1
print(cnt)