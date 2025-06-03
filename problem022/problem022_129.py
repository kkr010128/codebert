N = input()
S = set(map(int, input().split()))
Q = input()
T = set(map(int, input().split()))


intersection = S & T
print(len(intersection))
