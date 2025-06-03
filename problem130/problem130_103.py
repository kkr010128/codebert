def first_three(str):
	return str[:3] if len(str) > 3 else str
  
val = input()
print(first_three(val))