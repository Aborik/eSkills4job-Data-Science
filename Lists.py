# ### Creating an empty list
# eampty_list = list()
# print(eampty_list)

# # crearting another with
# list_num = list([1, 2, 3, 4])
# print(list_num)

list_num2 = [5, 6, 7]
# print(list_num2[1])

# # To easliy iterate all elements the list
# for each_item in list_num2:
#     print(each_item)

# for each_item in range( 0, 3):
#     print(list_num2)


house_items = ["cat", 3, "dog", 2, "tv", "boys"]
for i in range (0, 6):
    print(house_items[i])


house_items = ["cat", 3, "dog", 2, "tv", "boys"]
for i in range (0, len(house_items)):
    print(house_items[i])
print("-------------------------------------")
### List slicing
print(house_items[0:2])
print(house_items[2:6])
print("-------------------------------------")
## Adding items
house_items.append("girls")
print("-------------------------------------")
# Extend a list
house_items.extend(list_num2)
print( house_items)
print("---------------------------------------")

## Insect an intem in a specific index
house_items.insert(0, "pen")
print(house_items)

### Creating an empty list
fav_sport = []
# now ask the user their fav sports
user_input = input("What is your fav sport:")
fav_sport.append(user_input)
print(fav_sport)

