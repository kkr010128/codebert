K = int(input())
S = str(input())

if K >= len(S):
    answer = S
else:
    answer = (S[:K]+'{}'.format('...'))
print(answer)