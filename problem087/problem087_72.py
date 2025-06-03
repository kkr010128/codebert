N = int(input())
def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)
if digitSum(N) % 9 == 0:
  print("Yes")
else:
  print("No")