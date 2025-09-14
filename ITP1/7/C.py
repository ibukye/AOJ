r, c = map(int, input().split())
sheet = [[0 for _ in range(c+1)] for _ in range(r+1)]
for i in range(r):
    row = list(map(int, input().split()))
    row_sum = sum(row)
    for j in range(c):
        sheet[i][j] = row[j]
    sheet[i][j+1] = row_sum

for i in range(c+1):
    col_sum = 0
    for j in range(r):
        col_sum += sheet[j][i]
    sheet[j+1][i] = col_sum

for i in range(r+1):
    row = sheet[i]
    print(" ".join(map(str, row)))
