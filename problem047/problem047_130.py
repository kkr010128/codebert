while 1:
  input_a , op , input_b = map( str , raw_input().split() )
  a = int( input_a )
  b = int( input_b )
  if op == '+':
      print a + b
  elif op == '-':
      print a - b
  elif op == '*':
      print a * b
  elif op == '/':
      print a / b
  else:
      break