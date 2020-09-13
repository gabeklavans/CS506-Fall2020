from random import random

def draw_lake(numFish=3):
  # Make sure user didn't put in a number that was too high
  numFish = 8 if numFish > 8 else numFish
  # Same for too low
  numFish = 0 if numFish < 0 else numFish
  
  total_fish = 8
  fish = []
  for i in range(numFish):
    if random() > 0.5:
      fish.append("<O")
    else:
      fish.append("O>")

  for i in range(total_fish-numFish):
    fish.append("  ")

  print("""
     ____^-------       _____________________
    / ---------\ \     / ------------------- \ 
   / /          \ \___/ /       %s          \ \_
  | |    %s      \ ----/                      | |
  | |                          ^-^-^          | |
  | |  ^-^-^                   %s             | |
   \ \             %s                         | |
    \ \                               %s     /  /
     \ \____           ^-^-^                /  /
       -----  \              %s             | |
             \ \   %s                        \ \ 
              \ \           ^-^-^   %s     /-___|
              | |__________     __________/ /
              \ ____________/^\ ___________/
  """ % tuple(fish))        
  return
