n = int(input())
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
#s = input()


t = n % 10
if t == 2 or t == 4 or t == 5 or t == 7 or t == 9:
    print("hon")
elif t == 0 or t == 1 or t == 6 or t == 8:
    print("pon")
else:
    print("bon")

