from collections import deque

n, q = map(int, input().split())
name = deque()
time = deque()
for i in range(n):
    tmp_name, tmp_time = input().split()
    name.append(tmp_name)
    time.append(int(tmp_time))

ans_time = 0

while len(time)>0:
    tmp_time = time.popleft()
    tmp_name = name.popleft()
    if tmp_time<=q:
        ans_time += tmp_time
        print(tmp_name + " " + str(ans_time))
    else:
        ans_time += q
        time.append(tmp_time-q)
        name.append(tmp_name)