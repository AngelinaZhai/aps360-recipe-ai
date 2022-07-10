# data and partial code from: https://dominikschmidt.xyz/simplified-recipes-1M/

import numpy as np
import array

with np.load('simplified-recipes-1M.npz', allow_pickle=True) as data:
    # recipes = data['recipes']
    ingredients = data['ingredients']

print("Master ingredients list loading complete.")

# print(recipes[0])
# print(ingredients[0])

# sorted_ing = sorted(ingredients)
# print(sorted_ing[0])

# for i in range (0, len(sorted_ing)):
#     if (sorted_ing[i] == "milk"):
#         print("found")
#         break;

# print(ingredients)

    