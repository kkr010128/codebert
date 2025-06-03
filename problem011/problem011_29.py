data = list(map(int,input().split()))
if(data[0] < data[1]): data[0],data[1] = data[1],data[0]

def gcd(x,y):
    return x if y == 0 else gcd(y,x%y)

print(gcd(data[0],data[1]))
