# B - Multiple of 9

n = input()
print('Yes' if sum(int(d) for d in n) % 9 == 0 else 'No')
