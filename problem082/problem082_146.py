S = input()
T = input()

iteration = len(S) - len(T) + 1

if T in S:
    ans = 0
else:
    minimum = len(T)
    for i in range(iteration):
#         print('---------------')
        s = S[i:len(T)+i]
#         print(s)
#         print(T)
        count = 0
        for j in range(len(T)):
            if s[j] != T[j]:
                count += 1
#             print(count)
        minimum = min(minimum, count)
    ans = minimum
    
print(ans)