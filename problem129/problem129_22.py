n=int(input())
a=list(map(int,input().split()))
a.sort()

# 小さい側から処理する。a[i]について、10**6 以下のすべての倍数をset()として持つ。
# ただし、set内に存在しない==初出の約数のみ倍数計算をしてカウントする。
# 例えば、2,6,... となった場合、(6の倍数セットは2の倍数セットの下位集合となるため計算不要)

s=set()
cnt=0
for i,aa in enumerate(a):
  if aa not in s:
    # 同値が複数ある場合、カウントしない。sortしているため、同値は並ぶ
    if i+1 == len(a) or aa != a[i+1]:
      cnt+=1
    
    for i in range(1,10**6+1):
      ma=aa*i
      if ma > 10**6:
        break
      s.add(ma)

print(cnt)
    
