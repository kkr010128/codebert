sec=int(input())
print(":".join(map(str, [int(sec/3600), int(sec/60)%60, sec%60])))