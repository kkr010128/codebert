f=[1,1]
for _ in range(2,45):f+=[sum(f[-2:])]
print(f[int(input())])
