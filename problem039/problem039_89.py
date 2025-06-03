from sys import stdin

a, b, c = (int(n) for n in stdin.readline().rsplit())

answer = "Yes" if a < b < c else "No"

print(answer)

