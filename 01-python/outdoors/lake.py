from random import random

def draw_lake(numFish=3):
  # Make sure user didn't put in a number that was too high
  if numFish > 8:
    raise ValueError("There can be at max 8 fish in the pond")
  # Same for too low
  if numFish < 0:
    raise ValueError("There cannot be a negative number of fish in the pond")
  
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
