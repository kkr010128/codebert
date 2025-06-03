N = int(input())
S = str(input())
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
answer = ''
for i in range(len(S)):
    num = alpha.index(S[i])+N
    if num > 25:
        num -= 26
    answer += alpha[num]
print(answer)