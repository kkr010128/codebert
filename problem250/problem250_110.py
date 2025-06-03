x = int(input())

def judge(n):
    for i in range(1, n // 2 + 1):
        if i == 1: continue
        if n % i == 0:
            return False
    return True

i = x
while True:
    if judge(i):
        print(i)
        break
    i += 1