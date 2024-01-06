#2.6.11: LAB - Operators and expressions – 2
#Scenario
#Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
#For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
#Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒ the most important thing is that the code produces valid results for valid input data.
#Test your code carefully. Hint: using the % operator may be the key to success.

#TEST DATA
#SAMPLE INPUT:  12  17  59      EXPECTED OUTPUT:    13:16
#SAMPLE INPUT:  23  58  642     EXPECTED OUTPUT:    10:40
#SAMPLE INPUT:  0   1   2939    EXPECTED OUTPUT:    1:0

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

complete_hours = dura // 60
remains_mins = dura % 60

mins = (mins + remains_mins) % 60
hour += complete_hours + ((mins + remains_mins) % 60)
print(hour, ":", mins)

