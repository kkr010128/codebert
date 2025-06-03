hp, count_skills = map(int, input().split())
a = map(int, input().split())
skills_list = list(a)

for skill in skills_list:
    hp -= skill
    if hp <= 0:
        print('Yes')
        break
if hp >= 1:
    print('No')
