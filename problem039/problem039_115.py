import sys

x = sys.stdin.readline()

a_list = x.split(" ")

if int(a_list[0]) < int(a_list[1]) and int(a_list[1]) < int(a_list[2]):
  print "Yes"

else:
  print "No"