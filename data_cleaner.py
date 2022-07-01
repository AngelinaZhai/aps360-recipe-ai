import csv

data = [] #total cleaned data array

# Reading AllRecipes CSV file
#['Recipe Name;Review Count;Recipe Photo;Author;Prepare Time;Cook Time;Total Time;Ingredients;Directions;RecipeID']
#   0           1               2          3        4           5           6           7         8         9
with open('allrecipes\clean_recipes.csv', mode='r') as f:
    read = f.readlines()
    for line in read:
        tmp1, tmp2 = [], []
        tmp1 += line.split(';')
        tmp2.append(tmp1[0]) #Recipe name
        tmp2.append(tmp1[2]) #Recipe photo URL
        tmp2.append(tmp1[7]) #Recipe Ingredients (need to splice later)
        tmp2.append(tmp1[8]) #Recipe cooking directions
        data.append(tmp2)

# print(data[3]) #sanity check

# tmp = []
# Reading Indian Food CSV file
# TranslatedRecipeName,TranslatedIngredients,TotalTimeInMins,Cuisine,TranslatedInstructions,URL,Cleaned-Ingredients,image-url,Ingredient-count
#           0                   1                  2            3               4            5          6               7           8
# with open('indian\Cleaned_Indian_Food_Dataset.csv', mode='r', encoding='utf-8') as f:
#     read = f.readlines()
#     for line in read:
#         # if (line == 1):
#         #     break
#         tmp1, tmp2 = [], []
#         tmp1 += line.split(',')
#         # print(len(tmp1))
#         # tmp2.append(tmp1[0]) #Recipe name
#         # tmp2.append(tmp1[7]) #Recipe photo URL
#         # tmp2.append(tmp1[6]) #Recipe Ingredients (need to splice later)
#         # tmp2.append(tmp1[4]) #Recipe cooking directions
#         # tmp.append(tmp2)

print(len(data))