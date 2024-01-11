# 3.2.15: LAB - Collatz's hypothesis

#       Scenario
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

#     take any non-negative and non-zero integer number and name it c0;
#     if it's even, evaluate a new c0 as c0 ÷ 2;
#     otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#     if c0 ≠ 1, go back to point 2.

# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), 
# but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.

# Test your code using the data we've provided.

# TEST DATA
# INPUT DATA    15      EXPECTED OUTPUT     46
#                                           46      expected output used in plataform is wrong, real answer is 23
#                                           70
#                                           35
#                                           106
#                                           53
#                                           160
#                                           80
#                                           40
#                                           20
#                                           10
#                                           5
#                                           16
#                                           8
#                                           4
#                                           2
#                                           1
#                                           steps = 17
# INPUT DATA    16      EXPECTED OUTPUT     8
#                                           4
#                                           2 
#                                           1
#                                           steps = 4
# INPUT DATA    1023    EXPECTED OUTPUT     3070
#                                           1535
#                                           4606
#                                           2303
#                                           6910
#                                           3455
#                                           10366
#                                           5183
#                                           15550
#                                           7775
#                                           23326
#                                           11663
#                                           34990
#                                           17495
#                                           52486
#                                           26243
#                                           78730
#                                           39365
#                                           118096
#                                           59048
#                                           29524
#                                           14762
#                                           7381
#                                           22144
#                                           11072
#                                           5536
#                                           2768
#                                           1384
#                                           692
#                                           346
#                                           173
#                                           173     expected output used in plataform is wrong, real answer is 520
#                                           260
#                                           130
#                                           65
#                                           196
#                                           98
#                                           49
#                                           148
#                                           74
#                                           37      
#                                           37      expected output used in plataform is wrong, real answer is 112
#                                           56
#                                           28
#                                           14
#                                           7
#                                           22
#                                           11
#                                           34
#                                           17
#                                           52
#                                           26
#                                           13
#                                           40
#                                           20
#                                           10
#                                           5
#                                           16
#                                           8
#                                           4
#                                           2       expected output don't show the 1 in this example, an error
#                                           steps = 62

#proposed code
# c0 = int(input("Enter with a natural number, except 0: "))
# steps = 0
# while True:
#     if c0 == 1:
#         #print(c0)
#         print("steps:", steps)
#         break
#     else:
#         if c0 % 2 == 0:     # even number
#             c0 = c0/2
#             print(int(c0))
#             steps += 1
#         else:               # odd number
#             c0 = 3 * c0 + 1
#             print(int(c0))
#             steps += 1

#a little beyond code
low_loop = int(input("Enter with the first hypothesis test number: "))
high_loop = int(input("Enter with the upper hypothesis test number: ")) + 1
i = low_loop
steps = 0

for i in range(low_loop, high_loop):
    c0 = i
    while True:
        if c0 == 1:
            # print("steps:", steps)
            break
        else:
            if c0 % 2 == 0:     # even number
                c0 = c0/2
                steps += 1
            else:               # odd number
                c0 = 3 * c0 + 1
                steps += 1
    print("number of steps for the number", i, "is", steps)
    steps = 0