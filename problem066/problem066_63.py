Card = input()
while Card != ("-"):
 m = int(input())
 H = [int(input()) for i in range(m)]
 for i in H:
  hcard = Card[0:i]
  Card = Card.replace(hcard, "", 1) + hcard
 print(Card)
 Card = input()