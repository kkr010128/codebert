W = input()
lis = []
cot = 0
while True:
    x = input().split()
    if x == ["END_OF_TEXT"]:
        break
    lis += x
for y in lis:
    if y.lower() == W:
        cot += 1
print(str(cot))



