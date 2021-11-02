# Debugging Problem

# Describe Problem

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")
# my_function()


# Reproduce the Bug
from random import randint
dice_imgs = ["1", "2", "3" ,"4" ,"5" ,"6"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num - 1])
