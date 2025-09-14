cards = [
    [0 for s in range(1, 14)], # S
    [0 for h in range(1, 14)], # H
    [0 for c in range(1, 14)], # C
    [0 for d in range(1, 14)]  # D
]
n = int(input())
for i in range(n):
    card_sign, card_num = input().split()   # ex) card_sign="S", card_num="10"
    card_num = int(card_num)
    if card_sign=="S":
        cards[0][card_num-1] = 1
    elif card_sign=="H":
        cards[1][card_num-1] = 1
    elif card_sign=="C":
        cards[2][card_num-1] = 1
    else:
        cards[3][card_num-1] = 1
sign = ["S", "H", "C", "D"]
for j in range(4):
    for k in range(13):
        if cards[j][k] == 0:
            print(f"{sign[j]} {k+1}")