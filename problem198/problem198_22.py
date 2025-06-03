# 使えるのは、'a' ~ 今まで使われた次の文字
n = int(input())
def dfs(cnt,s):
    if cnt == n:
        print(s)
        return
    biggest = 'a'
    c = 0
    while c < len(s):# 最後はどこまで？
        if s[c] == biggest:
            biggest = chr(ord(biggest)+1)
            c += 1
        else:
            c += 1
    #print(c)
    for i in range(0,ord(biggest) - ord('a')+1):
        sc = chr(ord('a') + i)
        #print(sc)
        s += sc
        dfs(cnt + 1, s)
        s = s[:-1]

dfs(0,"")
