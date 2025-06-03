a, b = map(int, input().split())

mini, big = (a, b) if a < b else (b, a)

while True:
    rem = big % mini
    if rem == 0:
        break
    mini, big = rem, mini

print(mini)