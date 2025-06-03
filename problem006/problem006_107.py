# coding: utf-8
#Problem Name: Debt Hell
#ID: tabris
#Mail: t123037@kaiyodai.ac.jp

n = float(raw_input())
dept = 100000
for i in range(int(n)):
    dept *= 1.05
    if not (dept/1000).is_integer():
        dept /= 1000
        dept = __import__('math',fromlist=['floor']).floor(dept)*1000+1000
print int(dept)