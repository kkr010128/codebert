n, x, t = map(int, input().split())

times = n/x
if times - int(times) > 0:
  times = int(times) + 1

time = times*t

print(int(time))