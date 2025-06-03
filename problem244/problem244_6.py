def is_much_money(num_of_coin, yen):
  if num_of_coin * 500 >= yen:
    return "Yes"
  else:
    return "No"
 
if __name__ == "__main__":
    num_of_coin, yen = input().split()
    judgement = is_much_money(int(num_of_coin), int(yen))
    print(judgement)