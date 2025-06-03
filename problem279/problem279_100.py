#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

n = int(input())
s = input()

if (n % 2 != 0):
    print("No")
    exit()

for i in range(n//2):
    if (s[i] != s[n//2 + i]):
        print("No")
        exit()
print("Yes")

