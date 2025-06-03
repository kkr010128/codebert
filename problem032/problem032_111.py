n = input()
x = list(map(int,raw_input().split()))
y = list(map(int,raw_input().split()))
gap = []
gap1 = 0.0
gap2 = 0.0
gap3 = 0.0
a = 0.0

for i in range(n):
    gap.append(abs(x[i]-y[i]))

for i in range(n):
    gap1 += gap[i]
print gap1

for i in range(n):
    gap2 += gap[i] ** 2  

print pow(gap2,0.5)

for i in range(n):
    gap3 += gap[i] ** 3
print pow(gap3,0.3333333333)

print max(gap)