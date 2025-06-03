def minko_n(x,y,n):
    D = 0
    for i in range(len(x)):
        D += (abs(x[i]-y[i]))**n
    return D**(1/n)

def minko_f(x,y):
    l = []
    for i in range(len(x)):
        l.append(abs(x[i]-y[i]))
    return max(l)

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

print(minko_n(x,y,1))
print(minko_n(x,y,2))
print(minko_n(x,y,3))
print(minko_f(x,y))
