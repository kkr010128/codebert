n = int(raw_input())
card = [i+" "+str(j) for i in "SHCD" for j in range(1,14)]
for i in range(n):
    card.remove(raw_input())
    pass
for i in  card:
    print i
