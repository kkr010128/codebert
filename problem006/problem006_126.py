n = input();

ans = 100000;
for i in range(n):
  ans = int(float(ans) * 1.05);
  ans += 999;
  ans /= 1000;
  ans *= 1000;

print ans 