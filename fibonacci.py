#   #############################################################################
#   Jordan Ramirez
#   Lab: 5
#   06/5/2022
#   To maximize profits, this program uses fibonacci retracement
#   ratios in order to offer the best possible entry and exit-points
#   given the particular stocks price movements within a certain time period.
#   Sources: Lesson 8 and below, python.org, PythonProgramming.in, w3schools.com
#   #############################################################################

# Calculating the Fibonacci Retracement Level Prices with a non-Fibonocci level/ratio of 50%
# Set constant float int f = 0.236, 0.382, 0.5, 0.618
f = [0.236, 0.382, 0.5, 0.618]

# Module welcome()
# Display welcome message
# Display "This program will help determine the perfect entry and exit price to maximize potential profits
# while exposing the least possible risk.
# End module

def welcome():
    print("Welcome to the Fibonacci Strategy!")
    print("\nThis program will help determine the perfect")
    print("\bentry and exit price to maximize profits,")
    print("while exposing the least possible risk.")

# Module main()
# Call welcome()
# Declare float int max_price
# Declare float int min_price
# Call fib_upward(max_price,min_price)
# End module
def main():
    welcome()
    max_price = 0.00
    min_price = 0.00
    max_price = float(input("\nEnter the securities highest closing price:$ "))
    min_price = float(input("Enter the securities lowest closing price:$ "))
    fib_upward(max_price,min_price)

# Module fib_upward(max,min)
# Set diff =  max - min
# Declare levels for upward trends 1-4 with num_level = max - (diff * f[0])
# Declare values = [first_lvl,sec_lvl,third_lvl,fourth_lvl]
# Declare length = len(values)
# Declare lowest entry_point = values[]
# Declare highest exit_point = values[]
# For index in range(length)
#       if values[index] > entry_point
#           Set entry_point = values[index]
#       if values[index] > exit_point
#           Set exit_point = values[index]
# Display "UPWARD TREND RETRACEMENT STRATEGY"
# Display ("Based on the information given, your entry-point should be:$", entry_point)
# Display ("AND your exit-point should be:$", exit_point)
# Call fib_downward(max,min)
#End module
def fib_upward(max,min):
    diff = max - min
    first_lvl = max - (diff * f[0])
    sec_lvl = max - (diff * f[1])
    third_lvl = max - (diff * f[2])
    fourth_lvl = max - (diff * f[3])
    values = [first_lvl, sec_lvl, third_lvl, fourth_lvl]
    length = len(values)-1
    entry_point = values[0]
    exit_point = values[0]
    for index in range(length):
        if values[index] < entry_point:
            entry_point = values[index]
        if values[index] > exit_point:
            exit_point = values[index]
    print("\nUPWARD TREND RETRACEMENT STRATEGY")
    print("-----------------------------------")
    print("Based on the information given,")
    print("your Entry-Point should be:$",entry_point)
    print("\bAND")
    print("\bYour Exit-Point should be:$",exit_point)

    fib_downward(max,min)

# Module fib_downward(max,min)
# Set diff =  max - min
# Declare levels for downward trends 1-4 with num_level = max + (diff * f[0])
# Declare values = [first_lvl,sec_lvl,third_lvl,fourth_lvl]
# Declare length = len(values)
# Declare lowest entry_point = values[]
# Declare highest exit_point = values[]
# For index in range(length)
#       if values[index] > entry_point
#           Set entry_point = values[index]
#       if values[index] > exit_point
#           Set exit_point = values[index]
# Display "DOWNWARD TREND RETRACEMENT STRATEGY"
# Display ("Based on the information given, your entry-point should be:$", entry_point)
# Display ("AND your exit-point should be:$", exit_point)
# Declare str ask
# Set input ask = "Would you like to enter another sequence?"
# If ask = y
#   Call main()
# Else End
# End Module
#Main()
def fib_downward(max,min):
    diff = max - min
    first_lvl = min + (diff * f[0])
    sec_lvl = min + (diff * f[1])
    third_lvl = min + (diff * f[2])
    fourth_lvl = min + (diff * f[3])
    values = [first_lvl, sec_lvl, third_lvl, fourth_lvl]
    length = len(values)
    entry_point = values[0]
    exit_point = values[0]
    for index in range(length):
        if values[index] < entry_point:
            entry_point = values[index]
        if values[index] > exit_point:
            exit_point = values[index]
    print("\nDOWNWARD TREND RETRACEMENT STRATEGY")
    print("---------------------------------------")
    print("Based on the information given,")
    print("your Entry-Point should be:$",entry_point)
    print("\bAND")
    print("\bYour Exit-Point should be:$",exit_point)

    ask = ''
    ask = input("Would you like to enter another sequence?: ")
    if ask == 'y' or ask == 'Y':
        main()
    else:
        return

main()

