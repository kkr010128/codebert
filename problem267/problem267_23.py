N = int(input())
S = input()

tried_first_digit = {}
tried_second_digit = {}
password = {}

for i in range(N-2):
    if S[i] not in tried_first_digit:
        tried_first_digit[S[i]] = 0
        for j in range(i+1, N-1):
            if S[i]+S[j] not in tried_second_digit:
                tried_second_digit[S[i]+S[j]] = 0
                for k in range(j+1, N):
                    if S[i]+S[j]+S[k] not in password:
                        password[S[i]+S[j]+S[k]] = 0

print(len(password))
