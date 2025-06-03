str = input()
def hitachi(S):
    hitachi_str = [True if S[i:i+2] == 'hi' else False for i in range(0,len(S),2)]
    if all(hitachi_str):
        result = 'Yes'
    else:
        result = 'No'
    return result
print(hitachi(str))