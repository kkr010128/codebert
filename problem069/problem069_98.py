def func(K):
  result = ""
  for i in range(K):
    result += "ACL"
  return result

if __name__ == "__main__":
    K = int(input())
    print(func(K))