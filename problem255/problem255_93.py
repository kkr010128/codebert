N = input()
S,T = input().split()
txt = ''
for si,ti in zip(S,T):
    txt += si+ti
print(txt)
