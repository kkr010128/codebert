n = int(input())
h = n // 3600
m = (n % 3600) // 60
s = n - (h * 3600) - (m * 60)
print('{0}:{1}:{2}'.format(h, m, s))