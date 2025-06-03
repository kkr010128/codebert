n = int(input())
s = list(input() for _ in range(n))

print(len(list(set(s))))