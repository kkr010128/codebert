n = int(input())
rounded = round(n, -3)
if rounded < n:
  rounded += 1000
print(rounded - n)