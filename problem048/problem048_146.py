n = int(input())
ai = input().split()
ai = list(map(int,ai))
ai.sort()

sum = 0

for i in ai:
    sum += i

print(ai[0],ai[n-1],sum)