import math
n=int(input())
nums=list(map(int,input().split()))
point_num=nums[0]
for i in range(1,n):
    lcm=point_num*nums[i]//math.gcd(point_num,nums[i])
    point_num=lcm
print(lcm)