#import re

N = input()
stones = input()
#pattern = 'W.*R'
#stoneslist =list(stones)
#result = re.search(pattern,stones)
#if result:
 # print (result.start())
  #print (result.end())
#print(stones[result.start()])
#stoneslist[result.start()]='R'
#stoneslist[result.end()-1]='W'

count =0
#while 'WR' in stones:
 # if stones.count('WR')>1:
  #  stoneslist =list(stones)
   # result = re.search(pattern,stones)
    #stoneslist[result.start()]='R'
    #stoneslist[result.end()-1]='W'
    #stones =str(stoneslist)
    #stones = "".join(stoneslist)
  #else:
   # stones = stones.replace('WR','RR',1)
  #count+=1
  #print(stones)

#print (stones)

red = 0
white = 0
for i in range(len(stones)):
  if stones[i] == "R":
    red +=1
for i in range(red):
  if stones[i] =='W':
    white+=1
print (white)
#print (count)