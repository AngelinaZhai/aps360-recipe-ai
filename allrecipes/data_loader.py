import csv
import os

data = [] #total cleaned data array

# Reading AllRecipes CSV file
#['Recipe Name;Review Count;Recipe Photo;Author;Prepare Time;Cook Time;Total Time;Ingredients;Directions;RecipeID']
#   0           1               2          3        4           5           6           7         8         9
with open('clean_recipes.csv', mode='r') as f:
    read = f.readlines()
    n = -1
    for line in read:
        tmp1, tmp2 = [], []
        tmp1 += line.split(';')
        tmp2.append(tmp1[0]) #Recipe name
        tmp2.append(tmp1[2]) #Recipe photo URL
        tmp2.append(tmp1[7].split(',')) #spliced cleaned ingredients
        tmp2.append(tmp1[8].split('**')) #spliced cooking directions
        tmp2.append(n)
        data.append(tmp2) #add to total list
        n += 1

del data[0] #remove label row


print("Loading Done.")
