n = int(raw_input())
num = map(int, raw_input().split())
num.reverse()
print " ".join(map(str, num))
