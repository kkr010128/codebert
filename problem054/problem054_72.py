n = int(input())
l = [0]*53
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == "H":
        b += 13
    elif a == "C":
        b += 26
    elif a == "D":
        b += 39
    l[b] = 1 
for j in range(1,53):
    if l[j] != 1:
         ama = j % 13
         syou = j // 13
         if ama == 0:
             ama = 13
             syou -= 1 
         if syou == 0:
             zi = "S"
         elif syou == 1:
             zi = "H"
         elif syou == 2:
             zi = "C"
         else:
             zi = "D"
         print(zi, ama)