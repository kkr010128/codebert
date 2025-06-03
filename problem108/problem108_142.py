N = int(input())
N %= 1000
change = 1000 - N
print(change if change != 1000 else 0)