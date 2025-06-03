# -*- coding:utf-8 -*-
class Cards:
    trump = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,]
    def HaveCards(self,num):
        self.trump[num] = True
    def TransCards(self,s,num):
        if(s == 'H'):
            num += 13 
        elif(s == 'C'):
            num +=26  
        elif(s == 'D'):
            num += 39
        return num
    def CheckCards(self,num):
        if(num <= 12):
            return 'S' ,num+1
        elif(num >= 13 and num <= 25):
            return 'H'  ,num-12
        elif(num >= 26 and num <= 38):
            return 'C',num-25
        elif(num >= 39 and num <=51):
            return 'D',num-38
        
n = int(input())
ob = Cards()
for i in range(n):
    s,str_num = input().split()
    number = int(str_num)
    Num=ob.TransCards(s,number-1)
    ob.HaveCards(Num)

for i in range(len(Cards.trump)):
    if Cards.trump[i] == False:
        Str,Num=ob.CheckCards(i)
        print(Str,Num)