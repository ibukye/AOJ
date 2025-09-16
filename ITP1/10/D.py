def min_distance(diff_abs,p):
    total=0
    for i in range(n):
        total+=(diff_abs[i])**p
    D_xy=(total)**(1/p)
    return D_xy
def chef_distance(diff_abs):
    return max(diff_abs)
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
diff_abs=[0 for _ in range(n)]
for i in range(n):
    diff_abs[i]=abs(x[i]-y[i])
for i in range(1,4):
    print(min_distance(diff_abs,i))
print(chef_distance(diff_abs))