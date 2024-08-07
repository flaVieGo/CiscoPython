# Slices – negative indices

# 1
# To repeat:
#     start is the index of the first element included in the slice;
#     end is the index of the first element not included in the slice.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) 


# 2
# If the start specifies an element lying further than the one described by the end (from the list's beginning), the slice will be empty:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) 


# 3
# If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)


# 4
# Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) 


# 5
# As we've said before, omitting both start and end makes a copy of the whole list:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)


# 6
# del instruction is able to delete more than just a list's elements at once ‒ it can delete slices too:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) 


# 7
# Deleting all the elements at once is possible too:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


# 8
# The del instruction will delete the list itself, not its content.
# The print() function invocation from the last line of the code will then cause a runtime error.
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) 