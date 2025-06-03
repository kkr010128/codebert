n = int(input())
s = [None] * n
for i in range(n):
    s[i] = input()
print(len(list(set(s))))