#coding:utf-8

n = int(input().rstrip())
toku =[0,0]
narabe = []

for i in range(n):
    taro, hana = input().rstrip().split()
    if taro == hana:
        toku[0] +=1
        toku[1] +=1

    else:
        narabe = [taro, hana]
        narabe.sort()
        toku[0] += narabe.index(taro)*3
        toku[1] += narabe.index(hana)*3
    
print(" ".join(list(map(str,toku))))