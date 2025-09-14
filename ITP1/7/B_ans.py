solution_way = []
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):          # i < j
            k = x - i - j
            if j < k <= n:                 # j < k  ここで範囲内か判定する
                count += 1
    solution_way.append(count)

print("\n".join(map(str, solution_way)))