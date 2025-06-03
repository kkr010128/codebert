def func(D,T,S):
  actualTime = D / S
  if actualTime <= T:
    return "Yes"
  else:
    return "No"


if __name__ == "__main__":
    inputStr = input().split(' ')
    D = int(inputStr[0])
    T = int(inputStr[1])
    S = int(inputStr[2])
    print(func(D,T,S))