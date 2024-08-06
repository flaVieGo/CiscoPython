# Removing elements from a list

# 1
numbers = [10, 5, 7, 2, 1]
del numbers[1]
print(len(numbers))
print(numbers)


# 2 - the following snippet will cause runtime errors, because you can't access an element which doesn't exist.
print(numbers[4])
numbers[4] = 1 


# 3
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
