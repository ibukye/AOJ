while True:
    x = input()
    if x == "0": break
    digit_sum = 0
    for i in range(len(x)):
        digit_sum += int(x[i])
    print(digit_sum)