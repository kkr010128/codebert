a, b, c = map(int, input().split())
divisitor = []
for i in range(a, b+1):
    if a < 0 or b < 0 or c < 0:
        break
    elif a > 10001 or b > 10001 or c > 10001:
        break
    elif a > b:
        break
    elif c % i == 0:
        divisitor.append(int(c/i))

print((len(divisitor)))