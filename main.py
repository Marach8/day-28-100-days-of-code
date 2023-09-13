import random, time, os

def char1():
  a = input('\033[33mWhat is your Character name: \033[0m')
  print()
  b = input('\033[35mWhat is your character type (human, imp, wizard, elf): \033[0m').lower()
  print()
  return a

def Health():
  a = random.randint(1, 6)
  b = random.randint(1, 12)
  c = int(((a*b)/2) + 10)
  return c

def Strength():
  a = random.randint(1, 6)
  b = random.randint(1, 12)
  c = int(((a*b)/2) + 12)
  return c

while True:
  print('\033[31m⚔️  BATTLE TIME ⚔️\033[0m')
  time.sleep(2)
  print()            

  fighter1 = char1()
  print(fighter1)
  time.sleep(2)
  health_stat1 = Health()
  print(f'HEALTH: {health_stat1}')
  time.sleep(1)
  strength1 = Strength()
  print(f'STRENGTH: {strength1}')
  print()
  
  time.sleep(2)
  print('\033[31mWho are they battling with?\033[0m')
  time.sleep(2)
  print() 
  
  fighter2 = char1()
  print(fighter2)
  time.sleep(2)
  health_stat2 = Health()
  print(f'HEALTH: {health_stat2}')
  time.sleep(1)
  strength2 = Strength()
  print(f'STRENGTH: {strength2}')
  print()
  
  time.sleep(3)
  os.system('clear')
  print('\033[31m⚔️  BATTLE TIME ⚔️\033[0m')
  time.sleep(2)
  print()
  print('\033[31mThe battle begins!\033[0m')
  print()

  x = 0
  while health_stat1 > 0 and health_stat2 > 0:    
    fighter1_roll = random.randint(1, 6)
    fighter2_roll = random.randint(1, 6)
  
    if fighter1_roll > fighter2_roll:
      time.sleep(6)
      e = int(abs(strength2 - strength1) + 1)
      print(f'\033[32m{fighter1} wins round {x} with the first blow\033[0m')
      time.sleep(2)
      print(f'\033[31m{fighter2} takes a hit, with {e} damage\033[0m')
      health_stat2 = health_stat2 - e
      print()
     
    elif fighter2_roll > fighter1_roll:
      time.sleep(6)
      e = int(abs(strength2 - strength1) + 1)
      print(f'\033[32m{fighter2} wins round {x} using smackdown\033[0m')
      time.sleep(2)
      print(f'\033[31mOh! no! {fighter1} takes a hit, with {e} damage\033[0m')
      health_stat1 = health_stat1 - e
      print()
    
    else:
      time.sleep(6)
      print(f'\033[36mNo winner, No vanquished for round {x}!\033[0m')
      print()
    
    time.sleep(2)  
    print(fighter1)
    time.sleep(2)
    print(f'HEALTH: {health_stat1}')
    print()
    
    time.sleep(2)
    print(fighter2)
    time.sleep(2)
    print(f'HEALTH: {health_stat2}')  
    print()
    time.sleep(3)
    

    if health_stat1 > 0 and health_stat2 > 0:
      print('And they are both standing for the next round!!!')
      time.sleep(4)
      os.system('clear')
      time.sleep(2)
      print()
      
      print('\033[31m⚔️  BATTLE TIME ⚔️\033[0m')
      time.sleep(2)
      print()
      print('\033[31mThe battle continues!\033[0m')
      print()
      x += 1
      
  if health_stat1 > health_stat2:
    print(f'Oh no! {fighter2} has died! 🤦‍♂️🤦‍♂️😭😭')
    print(f'''
{fighter1} has destroyed {fighter2} in just {x} rounds 😂😂😂😂
    ''')
  elif health_stat2 > health_stat1:
    print(f'Oh no! {fighter1} has died! 🤦‍♂️🤦‍♂️😭😭')
    print()
    print(f'\033[36m{fighter2} has destroyed {fighter1} in just {x} rounds! 😂😂😂😂\033[0m')
    print()
  time.sleep(2)
  ask = input('Do you want to play this game again? y/n: ').lower()
  if ask != 'y':
    break
print
time.sleep(2)
print('Byeeee! See you next time!')