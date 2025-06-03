#9_C
class player:
    def __init__(self):
        self.my_cards=[]
        self.point=0
    def draw(self,letter):
        self.my_cards.append(letter)

    def open(self,num):
        return self.my_cards[num]
    
    def buttle(self,letter,num):
        if(self.my_cards[num]>letter):
            self.point+=3
        elif(self.my_cards[num]==letter):
            self.point+=1
            
    def show(self):
        return self.point
    def check(self):
        return self.my_cards

##main##
n=int(input())
taro=player()
hanako=player()
for i in range(n):
    val=input().split()
    taro.draw(val[0])
    hanako.draw(val[1])
for i in range(n):
    taro.buttle(hanako.open(i),i)
    hanako.buttle(taro.open(i),i)
    
print(taro.show(),hanako.show())
    
