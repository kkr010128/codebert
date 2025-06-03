def min_dist(x_b,y_b):
    s=0
    for x,y in zip(x_b,y_b):
        s+=abs(x-y)
    return s

def man_dist(x_b,y_b):
    s=0
    for x, y in zip(x_b,y_b):
        s+=(abs(x-y))**2
    return s**0.5

def che_dist(x_b,y_b):
    s=0
    for x,y in zip(x_b,y_b):
        s+=(abs(x-y))**3
    return s**(1/3)

def anf_dist(x_b,y_b):
    s=[abs(x-y) for x,y in zip(x_b,y_b)]
    return max(s)

n=int(input())
x_b=list(map(int,input().split()))
y_b=list(map(int,input().split()))

print(min_dist(x_b,y_b))
print(man_dist(x_b,y_b))
print(che_dist(x_b,y_b))
print(anf_dist(x_b,y_b))