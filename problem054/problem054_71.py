n = int(input())
card =[i+" "+str(j) for i in ["S","H","C","D"] for j in range(1,14)]
for i in range(n):
    card.remove(input())
for i in card:
    print(i)
