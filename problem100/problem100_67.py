X = int(input())
up = 599
down = 400
i=8
while(i>=1):
    if(X <= up and X >= down):
        print(i)
        break
    else:
        up += 200
        down += 200
        i -= 1