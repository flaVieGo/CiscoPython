# Powerful Slices

# 1
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# this make just a copy of list_1, they are no more related.
# the part [:] used to say the elements of the copy
# [x:y] -> x is the start index and y is the end - 1
# "An element with an index equal to end is the first element which does not take part in the slicing."


# 2
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# 3
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)