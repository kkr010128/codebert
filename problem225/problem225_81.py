h, a = map(int, input().split())

if h % a == 0:
    print(int(h / a))

elif h % a != 0:
    print(int(h // a + 1))
