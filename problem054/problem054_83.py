n = input()
card = []
for i in range(n):
    card.append(raw_input())

for a in ['S','H','C','D']:
    for b in range(1,14):
        check = a +  " " + str(b)
        for c in card:
            if check == c:
                flg = 0
                break
            else:
                flg = 1
        if flg == 1:
            print check