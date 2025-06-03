n = input()
s, t = map(str, input().split())
out = [si+ti for si, ti in zip(s, t)]
print("".join(out))