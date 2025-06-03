n = int(input())
s = list(input())
abc_cnt = 0
cnt = 0
i = 0

while(i < n - 2):
    if(s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C'):
        cnt += 1
        if i < n -3:
            i = i+3
        else:
            i += 1
    else:
        i += 1

print(cnt)