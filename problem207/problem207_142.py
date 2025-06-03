card = []
for i in range(3):
    row = list(map(int,input().split()))
    card.append(row)

n = int(input())
ans = False

for i in range(n):
    b = int(input())
    for  j in range(3):
        if b in card[j]:
            card[j][card[j].index(b)] = 0

def judge(lst):
    return lst == [0,0,0]

for i in range(3):
    ans |= judge(card[i])
for i in range(3):
    ans |= judge([card[j][i] for j in range(3)])
ans |= judge([card[i][i] for i in range(3)])
ans |= judge([card[i][2-i] for i in range(3)])

print("Yes" if ans else "No")