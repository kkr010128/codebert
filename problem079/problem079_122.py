import math
#n個からr個とるときの組み合わせの数
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

S = int(input())
ans = 0
mod = 10 ** 9 + 7
for i in range(1,S // 3 + 1):      #長さiの数列のとき
   
    x = S - 3 * i       #3を分配後の余り
    
    ans += (combinations_count(x + i - 1, i - 1)) % mod  #重複組み合わせを足す
    ans %= mod

print(ans)
