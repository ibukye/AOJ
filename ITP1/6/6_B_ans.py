suits = ["S", "H", "C", "D"]
all_cards = {f"{s} {n}" for s in suits for n in range(1, 14)}

n = int(input())
for _ in range(n):
    all_cards.remove(input().strip())   # 入力されたカードを除外

for card in sorted(all_cards, key=lambda x: (suits.index(x[0]), int(x.split()[1]))):
    print(card)