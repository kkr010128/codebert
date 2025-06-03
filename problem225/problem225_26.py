#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

h,a = map(int, input().split())


ans = h // a
if (h % a != 0):
    ans += 1
print(ans)
