n = int(input())
ans = ['a'] # 最初の一文字は'a'で固定

for i in range(n-1): # 'a'に'n-1'文字分ループで足す
    tmp = [] # リセット
    for j in ans:
        l = len(set(j)) # 'j'の使用文字種の数をカウント
        for k in range(l+1): # 'j'の使用文字種の数 '+1'回ループして...
            tmp.append(j + chr(ord('a') + k)) # 'j'に appendする
    ans = tmp[:] # 'ans'を書き換える

for i in ans:
    print(i)
