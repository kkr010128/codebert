def count_pop(y):
  count = 0
  while y != 0:
    if y & 1 == 1:count+=1
    y = y >> 1
  return count
  
def main():
  N = int(input())
  X = input()
  X_val=int(X,2)
  X_pc=X.count('1')
  x_mod_pc_x_plus_1 = X_val % (X_pc + 1)
  x_mod_pc_x_minus_1 = X_val % max(X_pc - 1, 1)
  for i in range(N):
    if X[i] == '1':
      pc = X_pc - 1
      if pc == 0:
        print(0)
        continue
      val = (x_mod_pc_x_minus_1 - pow(2, N-i-1, pc)) % pc
    else:     
      pc = X_pc + 1
      val = (x_mod_pc_x_plus_1 + pow(2, N-i-1, pc)) % pc
    ans = 1   
    while val > 0:
      val %= bin(val).count('1')
      ans += 1
    print(ans)
  pass       
if __name__=='__main__':
  main()

