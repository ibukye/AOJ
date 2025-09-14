solution_way = []
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0: break
    solution_ = []
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if (i+j+k==x and i!=j and j!=k and i!=k):
                    count += 1
                    if (sorted([i, j, k]) not in solution_):
                        solution_.append(sorted([i, j, k]))
    solution_way.append(len(solution_))

print("\n".join(map(str, solution_way)))



