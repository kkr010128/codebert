input()
print(len([i for i in list(map(int,input().split()))[::2] if i%2]))