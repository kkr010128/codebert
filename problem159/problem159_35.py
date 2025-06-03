X = int(input())
n=0
m=100
while True:
    n+=1
    m+=m//100
    if m >=X:
        print(n)
        break