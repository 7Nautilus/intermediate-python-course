import random as r

def main():

  dice_rolls = int(input('Combien de dés veux-tu rouler? '))
  dice_size = int(input('Combien de faces auront les dés? '))
  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = r.randint(1,dice_size)

    if roll == 1:
      print(f'Tu as obtenu un {roll}! Dommage!')

    elif roll == dice_size:
      print(f'Tu as obtenu un {roll}! Super!')

    else:
      print(f'Tu as obtenu un {roll}')

    dice_sum += roll
  
  print(f'ton nombre de point total est de: {dice_sum} points')

if __name__== "__main__":
  main()