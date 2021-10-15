fruit = {"Banana": 5, "apple": 2, "orange": 3}
print(fruit)

#create fruit price dictionaries

fruit_price = {"Apple": 5,
                "banana": 4,
                "fig": 3}

print(fruit_price["Apple"]) # 5
print(fruit_price.get("banana")) #4
print(fruit_price.get("orange")) # none


fruit_selection = {"Apple": [5,6,7],"banana": 4, "fig": 3}

print(fruit_selection["Apple"][-2])