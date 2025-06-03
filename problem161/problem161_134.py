A, B, N = map(int, input().split())

def func(x):
    return (A*x)//B - A*(x//B)

print(func(min(B-1, N)))