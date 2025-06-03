N = int(input())
aaa = [int(i) for i in input().split()]

sumxor = 0
for a in aaa:
    sumxor = sumxor^a
bbb = [a^sumxor for a in aaa]
print(" ".join([str(b) for b in bbb]))