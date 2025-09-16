
while True:
    n=int(input())
    if n==0:break
    nums=list(map(int, input().split()))
    total=sum(nums)
    mean=total/n
    sub_total=0
    for i in range(n):
        sub_total+=(nums[i]-mean)**2
    variant=(sub_total/n)**0.5
    print(variant)
