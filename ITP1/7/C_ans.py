r, c = map(int, input().split())
sheet = [[0]*(c+1) for _ in range(r+1)]

for i in range(r):
    row = list(map(int, input().split()))
    row_sum = sum(row)
    for j, val in enumerate(row):
        sheet[i][j] = val
        sheet[r][j] += val     # 最下行に列合計を加算
    sheet[i][c] = row_sum
    sheet[r][c] += row_sum     # 右下の総合計

for i in range(r+1):
    print(" ".join(map(str, sheet[i])))
