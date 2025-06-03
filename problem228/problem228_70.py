h = int(input())
num = 0
t = 0
while h != 1:
    h = h//2
    num += 2**t
    t += 1
num += 2**t
print(num)