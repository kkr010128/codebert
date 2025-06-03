oc, cap, time = map(int, input().split())
cnt = 0
while oc>0:
    oc -= cap
    cnt += time

print(cnt)
