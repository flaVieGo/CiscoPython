# 3.1.6: LAB - Variables: Questions and Answers

#       Scenario
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer,
# and prints False if n is less than 100, and True if n is greater than or equal to 100.
# Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

#TEST DATA
# SAMPLE INPUT: 55      EXPECTED OUTPUT: False
# SAMPLE INPUT: 99      EXPECTED OUTPUT: False
# SAMPLE INPUT: 100     EXPECTED OUTPUT: True
# SAMPLE INPUT: 101     EXPECTED OUTPUT: True
# SAMPLE INPUT: -5      EXPECTED OUTPUT: False
# SAMPLE INPUT: +123    EXPECTED OUTPUT: True

n = int(input("Enter a number, anyone: "))
print(n >= 100)