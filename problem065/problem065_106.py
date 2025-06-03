import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

W = str_input()

cnt = 0
while 1:
    S = str_input()

    if (S == "END_OF_TEXT"):
        break

    S = S.lower().split()

    cnt += S.count(W)

print cnt