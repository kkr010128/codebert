n=int(input())
arr=list(map(int,input().split()))
xors = 0
for val in arr: #あらかじめすべての要素のxorを求めておく
 xors^=val #(ai xor aj = bi xor bj)となるのですべてのxorを合わせると、b0^b1^b2^...^bn
ans=[]
for i in range(n): #各aiについて、ai xor (すべての要素のxor)がi番目に書かれた値に等しい
 ans.append(xors^arr[i])
print(*ans)