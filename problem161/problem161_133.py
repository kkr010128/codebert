# ABC 165 D - Floor Function

a,b,n = map(int, input().split())

def func(i):
    return int(i*a/b) - a*int(i/b)

print(func(min(b-1, n)))