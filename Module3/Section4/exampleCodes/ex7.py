# Lists in action

# 1 - the python way to swap variables
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1 

# 2 - now, using lists
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list) 

# 3 - in a easy way for n elements
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list) 