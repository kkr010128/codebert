n=input()
print(sum(i&1 for i in list(map(int, input().split()))[::2]))