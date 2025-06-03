def ALDS1_3A():
  stk, RPexp = [], list(input().split())
  for v in RPexp:
      if v in '+-*':
          n2, n1 = stk.pop(), stk.pop()
          stk.append(str(eval(n1+v+n2)))
      else:
          stk.append(v)
  print(stk.pop())

if __name__ == '__main__':
    ALDS1_3A()