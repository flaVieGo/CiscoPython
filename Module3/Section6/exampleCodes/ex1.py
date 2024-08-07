# The inner life of lists

# 1
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# the changes in list_1 will affect the behavior in list_2, more in the below explanation:
# 
#  You could say that:
#     the name of an ordinary variable is the name of its content;
#     the name of a list is the name of a memory location where the list is stored.
# 
# Read these two lines once more ‒ the difference is essential for understanding what we are going to talk about next.
# 
# The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.