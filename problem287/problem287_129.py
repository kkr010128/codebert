a = list(set([i*j for i in range(1,10) for j in range(1, 10)]))
n = int(input())
print('Yes' if n in a else 'No')