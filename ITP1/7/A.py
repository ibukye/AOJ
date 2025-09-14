m, f, r = 0, 0, 0
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1: break
    if m == -1 or f == -1: print("F"); continue  # 中間試験、期末試験のいずれかを欠席した場合
    sum_score = m + f
    if (sum_score >= 80): print("A")
    elif (65 <= sum_score < 80): print("B")
    elif (50 <= sum_score < 65): print("C")
    elif (30 <= sum_score < 50): 
        if (r >= 50): print("C")
        else: print("D")
    elif (sum_score < 30): print("F")