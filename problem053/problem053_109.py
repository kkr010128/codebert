count = int(raw_input())

arr = map(int, raw_input().split())
arr.reverse()

print(" ".join(map(str, arr)))