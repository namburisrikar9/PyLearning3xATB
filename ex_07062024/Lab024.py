# Escape Sequence

print("Hello \"World\"")
print("Hello \nWorld") # Next line
print("Hello \tWorld") # Tab
print("Hello \bWorld") # Back


# list -> shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(type(shopping_list))
print(shopping_list[-1])
print(shopping_list[2])

shopping_list.append("curd") # Add item in the end - it will add end of list
print(shopping_list)

shopping_list.insert(1, "jam") # add item in middle
print(shopping_list)

shopping_list.extend(["chips", "Salt"]) # Add multiple item in the end
print(shopping_list)

shopping_list.remove("bread")
print(shopping_list)

print(shopping_list.pop()) #it will remove last item

print(shopping_list.index("butter"))# return on first value

shopping_list.reverse() # Reverse that order
print(shopping_list)

shopping_list.sort() # sort by order
print(shopping_list)

shopping_list[1] ="Srikar" # replace existing value
print(shopping_list)


#my_list = [1, 2, 3, 4, True, 3.14, "srikar"]
#print(my_list)
#print(type(my_list))


