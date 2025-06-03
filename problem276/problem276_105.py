n = int(input())
a = list(map(int, input().split()))
l = sum(a)
accu = 0
for i in a:
    accu += i
    if accu>l/2:
        if abs(l/2-accu)<abs(l/2-accu+i):
            print(accu*2-l)
        else:
            print(l-(accu-i)*2)
        break