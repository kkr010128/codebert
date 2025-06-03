N, M = map(int, input().split())
aaa = list(map(int, input().split()))
acc = sum(aaa)
print('Yes' if sum(4 * M * a >= acc for a in aaa) >= M else 'No')
