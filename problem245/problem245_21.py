N = int(input())
S = input()
l = [S[i:i+3] for i in range(0, len(S)-2)]
print(l.count('ABC'))    

