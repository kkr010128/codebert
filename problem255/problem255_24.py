n = int(input())
s, t = input().split()
combination_of_letters = ''
for i in range(n):
    combination_of_letters += s[i] + t[i]

print(combination_of_letters)