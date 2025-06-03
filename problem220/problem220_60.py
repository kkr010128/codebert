s = input().split()
n = list(map(int, input().split()))
U = input()
n[s.index(U)] -= 1
print(n[0], n[1])