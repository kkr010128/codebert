k = int(input())
s = str(input())

mod = 1000000007
decided_keta = len(s)
all_keta = len(s) + k

kai_list = [1 for i in range(2000010)]
for i in range(2,len(kai_list)):
    kai_list[i] = (kai_list[i-1]*i)%mod

answer = 0
for last_given_character_posi in range(decided_keta-1,all_keta):
    given_posi_pattern = kai_list[last_given_character_posi]*pow(kai_list[decided_keta-1],mod-2,mod)%mod*pow(kai_list[last_given_character_posi-decided_keta+1],mod-2,mod)%mod
    char_pattern = pow(25,last_given_character_posi-(decided_keta-1),mod)
    rest_char_pattern = pow(26,all_keta-(last_given_character_posi+1),mod)
    answer = (answer + given_posi_pattern*char_pattern%mod*rest_char_pattern%mod)%mod
print(answer)