n = int(input())
S = input()
l = len(S)

S += 'eeee'

cnt = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            # tmp = str(i)+str(j)+str(k)
            m = 0
            while S[m] != str(i):
                m += 1
                if m >= l:
                    break
            m += 1
            while S[m] != str(j):
                m += 1
                if m >= l:
                    break
            m += 1
            while S[m] != str(k):
                m += 1
                if m >= l:
                    break
            if m < l:
                cnt += 1

print(cnt)
