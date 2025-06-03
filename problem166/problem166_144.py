S = input()
mod2019 = [0]*len(S)

mod2019[-1] = int(S[-1])
keta_mod = 1
for i in range(len(S)-2,-1,-1):
    keta_mod = (keta_mod*10)%2019
    mod2019[i] = (mod2019[i+1] + int(S[i])*keta_mod)%2019

mod2019.extend([0])

answer = 0
count = [0 for _ in range(2020)]

for i in range(len(S)+1):
    answer += count[mod2019[i]]
    count[mod2019[i]] += 1
print(answer)
