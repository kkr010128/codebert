def main():
  n = int(input())
  a = list(map(int, input().split()))
  a.append(-1)
  num_kabu = 0
  money = 1000
  for i in range(0, n):
    if a[i+1] >= a[i]:
      num_kabu += money//a[i]
      money %= a[i]
    if a[i+1] <a[i]:
      money += num_kabu*a[i]
      num_kabu = 0
  print(money)
  
if __name__ =="__main__":
  main()