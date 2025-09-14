n, m = map(int, input().split())

a = [[[0] for _ in range(m)] for _ in range(n)]
b = [[0] for _ in range(m)]
c = [[0] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = row[j]
for i in range(m):
    b[i] = int(input())


for j in range(n):
    sum = 0
    for k in range(m):
        sum += a[j][k]*b[k] 
    c[j] = sum

print("\n".join(map(str, c)))