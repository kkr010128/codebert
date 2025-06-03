import collections
calc_time = 0
hoge = collections.deque()
num, q = [int(x) for x in input().split()]
for _ in range(num):
    name, t = input().split()
    hoge.append([name, int(t)])
while hoge:
    name, t = hoge.popleft()
    if t - q > 0:
        hoge.append([name, t-q])
        calc_time += q
    elif t == q:
        calc_time += q
        print ('{} {}'.format(name, calc_time))
    elif t - q < 0:
        calc_time += t
        print ('{} {}'.format(name, calc_time))
