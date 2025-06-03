def get_score(medium, final, retry):
    medium_final = medium + final
    if medium == -1 or final == -1:
        return 'F'
    elif 80 <= medium_final:
        return 'A'
    elif 65 <= medium_final:
        return 'B'
    elif 50 <= medium_final:
        return 'C'
    elif 30 <= medium_final:
        if 50 <= retry:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'


data = []
while True:
    [medium, final, retry] = [int(x) for x in raw_input().split()]
    if [medium, final, retry] == [-1, -1, -1]:
        break
    data.append(get_score(medium, final, retry))

for n in data:
    print(n)