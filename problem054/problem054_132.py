n=input()
s=range(1,14)
h=range(1,14)
c=range(1,14)
d=range(1,14)
trump={'S':s,'C':c,'H':h,'D':d}
for i in range(n):
    suit,num=raw_input().split()
    num=int(num)
    trump[suit].remove(num)
count=0
for suit in ['S','H','C','D']:
    for num in trump[suit]:
        print('%s %d'%(suit,num))