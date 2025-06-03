def main():
  N, M = list(map(lambda n: int(n), input().split(" ")))
  if M == 0:
    print("0 0")
    return 0

  AC = [0] * N
  WA = [0] * N

  for i in range(M):
    tmp = input().split(" ")
    No = int(tmp[0]) - 1
    if tmp[1] == "AC":
      AC[No - 1] = 1
    if tmp[1] == "WA" and AC[No - 1] == 0:
      WA[No - 1] += 1
  
  totAC = sum(AC)
  totWA = sum([AC[i] * WA[i] for i in range(len(AC))])
  print(totAC, end=" ")
  print(totWA)
    
main()
