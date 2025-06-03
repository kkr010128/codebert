from itertools import combinations as comb
def get_ans(m, n):
    ans = sum(1 for nums in comb(range(1, min(m+1,n-2)), 2) if ((n-sum(nums)>0) and (n-sum(nums) > max(nums)) and (n-sum(nums)<=m)))
    return ans
      
while True:
    m, n = (int(x) for x in input().split())
    if m==0 and n==0:
        quit()
    ans = get_ans(m, n)
    print(ans)
