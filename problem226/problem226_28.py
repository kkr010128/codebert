# 入力
monster_hp, quantity_of_skills = map(int, input().split())
skills = map(int, input().split())
skills_list = list(skills)

# 処理
total_damages = 0
for i in skills_list:
    total_damages += i

if monster_hp <= total_damages:
    print('Yes')
else:
    print('No')