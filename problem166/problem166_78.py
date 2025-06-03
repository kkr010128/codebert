S = input()[::-1]

S_mod = [0] * (len(S)+1)
S_mod[0] = int(S[0])

d = 10

for i in range(len(S)-1):
    S_mod[i + 1] = (S_mod[i] + int(S[i+1])*d)%2019
    d = d * 10 % 2019

mod_count = [0] * 2019
for i in range(len(S_mod)):
    mod_count[S_mod[i]] += 1
    
count = 0
for i in range(2019):
    count += mod_count[i] * (mod_count[i] - 1) / 2

print(int(count))