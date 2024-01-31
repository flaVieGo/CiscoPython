# 3.2.17 SECTION QUIZ

# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# for i in range(1, 11):
#     # Line of code.
#     if i % 2 != 0:
#         # Line of code.
#         print(i)

# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# x = 1
# while x < 11:
#     # Line of code.
#     if x % 2 != 0: 
#         # Line of code.
#         print(x)
#     # Line of code.
#     x += 1

# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
# prefix = ""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Line of code.
#         break
#     # Line of code.
#     prefix = prefix + ch
# print(prefix)
#the answer in plataform don't use any new variable, just this line     print(ch, end="")

# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits,
# replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
# for digit in "0165031806510":
#     if digit == "0":
#         # Line of code.
#         print("x", end="")
#         # Line of code.
#         continue
#     # Line of code.
#     print(digit, end="")