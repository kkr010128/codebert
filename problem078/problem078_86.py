N=int(input())
MOD=10**9+7

in_9=10**N-9**N
in_0=10**N-9**N
nine_and_zero=10**N-8**N

ans=int(int(in_0+in_9-nine_and_zero)%MOD)

print(ans)