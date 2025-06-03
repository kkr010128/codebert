card_ = lambda:set([i for i in range(1, 14)])
n = int(input())
count = 0
card = {"S": card_(), "H": card_(), "C": card_(), "D": card_()}
while count < n:
    i = list(input().split(" "))
    card[i[0]] -= {int(i[1])}
    count += 1
 
mark = ["S", "H", "C", "D"]
for m in mark:
    for c in sorted(card[m]):
        print("%s %d" % (m, c))