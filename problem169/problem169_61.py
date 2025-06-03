n = int(input())

list_ = [0]*n
joshi_list = list(map(int, input().split()))[::-1]

for i,num in enumerate(joshi_list):
  list_[num-1]+=1

for num in list_:
  print(num)