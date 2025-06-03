N = int(input())
S = input()
d = {
    'R': {},
    'G': {},
    'B': {}
}
for i, s in enumerate(S):
    d[s][i] = True
answer = len(d['R']) * len(d['G']) * len(d['B'])
for r in d['R'].keys():
    for g in d['G'].keys():
        if 2 * r - g in d['B']:
            answer -= 1
        if 2 * g - r in d['B']:
            answer -= 1
        if ((r + g) % 2 == 0 and ((r + g) // 2) in d['B']):
            answer -= 1
            

print(answer)