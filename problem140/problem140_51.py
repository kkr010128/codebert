import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

s = input()
# question_count = s.count("?")
# max_str = {"point":0,"str":""}

# for i in range(2**question_count):
#     swap_str = ""
#     for j in range(question_count):
#         if ((i>>j)&1):
#             swap_str += "P"
#         else:
#             swap_str += "D"
#     check_str = str(s)
#     for char in range(question_count):
#         check_str = check_str.replace("?",swap_str[char],1)
    
#     point = 0
#     point += check_str.count("D")
#     point += check_str.count("PD")
#     if max_str["point"] < point:
#         max_str["point"] = point
#         max_str["str"] = check_str
#     print(point,check_str)
# print(max_str["str"])
print(s.replace("?","D"))