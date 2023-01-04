# Imports
import random
import os
from art import logo, vs
from game_data import data
def random_entry(list):
  rand_no = random.randint(0, len(data) - 1)
  entry = data[rand_no]
  data.pop(rand_no)
  return entry

option_a = random_entry(data)
option_b = random_entry(data)

def check_followers(option_a, option_b, choice):
  followers_a = int(option_a["follower_count"])
  followers_b = int(option_b["follower_count"])
  
  if choice == 'A':
    if followers_a > followers_b:
      return True
    else:
      return False
  elif choice == 'B':
    if followers_a < followers_b:
      return True
    else:
      return False

condition = True
score = 0

while  condition:
  print(logo)
  def get_print_statements(option_a, option_b):
    name_a = option_a["name"]
    name_b = option_b["name"]
    description_a = option_a["description"]
    description_b = option_b["description"]
    country_a = option_a["country"]
    country_b = option_b["country"]
    def a_or_an(description):
      if description[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return 'an'
      else: 
        return 'a'
      
    print(f"Compare A: {name_a}, {a_or_an(description_a)} {description_a}, from {country_a}")
    print(vs)
    print(f"Against B: {name_b}, {a_or_an(description_b)} {description_b}, from {country_b}")
  get_print_statements(option_a, option_b)
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  if check_followers(option_a, option_b, choice):
    if choice == 'A':
      option_b = random_entry(data)
    elif choice == 'B':
      option_c = option_b
      option_b = random_entry(data)
      option_a = option_c
    score += 1
    os.system('cls')
    print(f"You're right! Current Score: {score}")
    
  else:
    condition = False
    print(f"Sorry that's wrong. Your final score: {score}")
  
  