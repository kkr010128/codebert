'''
参考
https://www.hamayanhamayan.com/entry/2019/12/29/032305
https://qiita.com/c-yan/items/4724d67c171d82a2366a

パターン1：A,Bともに偶数またはA,Bともに奇数の場合
⇒そのままお互いに近づく…(B-A)/2
パターン2：A,Bのいずれかが奇数の場合
⇒左端（Aに近いほう）か、右端（Bに近いほう）のいずれかで1ターン待機後、お互いに近づく
'''
N, A, B = map(int, input().split())

def approach(x, y):
    return (B-A)//2

ans = 0

if A % 2 == B % 2:
    ans = approach(A, B)
else:
    if A <= (N-B):
        ans += A
        A = 1
        B -= ans
    else:
        ans += N - B + 1
        B = N
        A += ans
    ans += approach(A, B)

print(ans)
