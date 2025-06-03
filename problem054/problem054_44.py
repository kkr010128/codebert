n=int(input())
cards = [[s+" "+str(n) for n in range(1,14)] for s in ["S","H","C","D"]]
for _ in range(n):
    suit,num =input().split()
    if suit=="S":
        cards[0][int(num)-1]=0
    elif suit=="H":
        cards[1][int(num)-1]=0
    elif suit=="C":
        cards[2][int(num)-1]=0
    elif suit=="D":
        cards[3][int(num)-1]=0
for s in cards:
    for n in s:
        if n!=0:
            print(n)