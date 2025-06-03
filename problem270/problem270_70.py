s=input()
dict1={7:'SUN',6:'MON',5:'TUE',4:'WED',3:'THU',2:'FRI',1:'SAT'}
keys = [k for k, v in dict1.items() if v == s]
print(keys[0])