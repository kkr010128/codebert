a = int(input())
s = 100000
for i in range(a):
        s = s * 1.05
        if s % 1000:
                s = s - (s % 1000) + 1000
print(int(s))
