N = int(input())
S = input()
total = 0

for i in range(N-2):
    if S[i] == "R":
        num_G = S[i+1:].count('G')
        num_B = S[i+1:].count('B')
        total += num_G * num_B
    elif S[i] == "G":
        num_B = S[i+1:].count('B')
        num_R = S[i+1:].count('R')
        total += num_B * num_R
    elif S[i] == "B":
        num_G = S[i+1:].count('G')
        num_R = S[i+1:].count('R')
        total += num_G * num_R

for i in range(N-2):
    for j in range(i+1, N-1):
        if 2*j-i >= N:
            continue
        if S[j] != S[i] and S[2*j-i] != S[j] and S[2*j-i] != S[i]:
            total -= 1

print(total)
