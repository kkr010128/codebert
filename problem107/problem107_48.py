# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
S = readline().decode().rstrip()
one_cnt = S.count('1')
S_rev = S[::-1]
#one_modは元のビットが立ってるとき zero_modは逆
one_mod = 0
zero_mod = 0
#Nが大きすぎるため下の桁から順に計算
for i in range(N):
    if S_rev[i] == '1' and one_cnt - 1 != 0:
        one_mod += pow(2,i,one_cnt - 1)
        one_mod %= (one_cnt - 1)
        zero_mod += pow(2,i,one_cnt + 1)
        zero_mod %= (one_cnt + 1)

cnt = [0]*(one_cnt+1)
pop_cnt = [0]* (one_cnt+1)
for i in range(1,one_cnt+1):
    pop_cnt[i] = pop_cnt[i//2] + i%2
    j = i % pop_cnt[i]
    cnt[i] = 1 + cnt[j] 

one_pow2 = [1]*(N+1)
zero_pow2 = [1]*(N+1)
for i in range(1,N):
    if one_cnt-1 != 0:
        one_pow2[i+1] = one_pow2[i]*2 % (one_cnt - 1)
    zero_pow2[i+1] = zero_pow2[i]*2 % (one_cnt + 1)

for i in range(N):
    if S[i] == '1':
        if one_cnt-1 == 0:
            print(0)
        else:
            nxt = one_mod
            nxt -= one_pow2[N-i]
            nxt %= (one_cnt - 1)
            print(1+cnt[nxt])
    else:
        nxt = zero_mod
        nxt += zero_pow2[N-i]
        nxt %= (one_cnt + 1)
        print(1+cnt[nxt])