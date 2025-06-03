HP, N = map(int, input().split())
ATK = list(map(int, input().split()))
print('Yes' if sum(ATK) >= HP else 'No')