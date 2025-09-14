n, m, l = map(int, input().split())

a = [[0 for _ in range(m)] for _ in range(n)]
b = [[0 for _ in range(l)] for _ in range(m)]
c = [[0 for _ in range(l)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = row[j]
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(l):
        b[i][j] = row[j]

"""
a -> n x m
b -> m x l
c -> n x l

=> a[n][m] * b[m][l] = c[n][l]

    a[0][0]*b[0][0]
+   a[1][0]*b[0][1]
+   a[2][0]*b[0][2]

これは、行列aの行 × 行列bの列で積を取り、cの要素を構成するという正しい行列積の考え方
つまり：
- a[i][k] * b[k][j] を k で合計して c[i][j] を作る
- i は a の行、j は b の列、k は共通の次元（m）

"""
"""
for i in range(n):
    total = 0
    for j in range(m):
        for k in range(l):
            total += a[i][j] * b[j][k]
            c[i][k] = total
"""

for i in range(n):          # aの行
    for j in range(l):      # bの列   
        total = 0
        for k in range(m):  # 共通次元
            total += a[i][k] * b[k][j]
        c[i][j] = total

for i in range(n):
    print(" ".join(map(str, c[i])))
