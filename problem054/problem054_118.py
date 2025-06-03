n=int(input())
suit = ["S","H","C","D"]
card = {i:[] for i in suit}
for i in range(n):
   tmp = ([c for c in input().split()])
   card[tmp[0]].append(tmp[1])

for i in suit:
    for j in range(1,14):
        if not (str(j) in card[i]):
            print("%s %s" % (i,j))