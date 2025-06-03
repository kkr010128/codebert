MOD = 10**9 + 7
def main():
  N, K = map(int , input().split())
  A = list(map(int, input().split()))
  
  if max(A) < 0 and K % 2 == 1:
    A.sort(reverse = True)
    ans = 1
    for i in range(K):
      ans = ans*A[i]%MOD
    print(ans%MOD)
  elif K == N:
    ans = 1
    for i in A:
      ans = ans*i%MOD
    print(ans%MOD)
  else:
    A_p = []
    A_m = []
    for i in A:
      if i >= 0:A_p.append(i)
      else:A_m.append(abs(i))
    A_p.sort(reverse =  True)
    A_m.sort(reverse = True)
    num = 0
    ans = 1
    posi_p = 0
    posi_m = 0
    sign = 0
    while (num < K):
      if posi_m == len(A_m) and posi_p < len(A_p):
        ans = ans*A_p[posi_p]%MOD
        posi_p += 1
        num += 1
      elif posi_p == len(A_p) and posi_m < len(A_m):
        ans = ans*A_m[posi_m]%MOD
        sign += 1
        posi_m += 1
        num += 1        
      elif  A_p[posi_p] >= abs(A_m[posi_m]):
        ans = ans*A_p[posi_p]%MOD
        posi_p += 1
        num += 1        
      else:
        ans = ans*A_m[posi_m]%MOD
        sign += 1
        posi_m += 1
        num += 1
      if num == K and sign % 2 == 1:
        if K == 1:
          ans = A_p[0]
        elif posi_m == len(A_m):
          ans = ans*pow(A_m[posi_m-1], MOD-2, MOD) % MOD
          ans = ans*A_p[posi_p] % MOD
        elif posi_p == len(A_p):
          ans = ans*pow(A_p[posi_p-1],  MOD-2, MOD)
          ans =  ans*A_m[posi_m] % MOD
        elif A_p[posi_p]*A_p[posi_p-1] >= A_m[posi_m]*A_m[posi_m-1]:
          ans = ans*pow(A_m[posi_m-1], MOD-2, MOD)%MOD
          ans = ans*A_p[posi_p] % MOD
        else:
          if posi_p != 0:
            ans = ans*pow(A_p[posi_p-1], MOD-2, MOD)%MOD
            ans = ans*A_m[posi_m]%MOD
          else:
            ans = ans*pow(A_m[posi_m-1], MOD-2, MOD)%MOD
            ans = ans *A_p[posi_p]%MOD
            
    print(ans%MOD)
          
    
if __name__ == "__main__":
  main()