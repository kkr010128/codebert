while True:
    s = input()
    if s == '-': break
    l = sum([int(input()) for _ in range(int(input()))]) % len(s)
    print(s[l:]+s[:l])