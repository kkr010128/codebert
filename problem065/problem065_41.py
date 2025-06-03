count = 0
W = input().lower()
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    count += T.lower().split().count(W)
print(count)