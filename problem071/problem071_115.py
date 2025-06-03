s = input()
if(len(s)==0):
  print("")
if(s[-1] == "s"):
  print(s+"es")
if(s[-1] != "s"):
  print(s+"s")