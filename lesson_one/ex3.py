# Enter Calculation: 5 * 6
# 5 * 6 = 30

# store the user input of 2 numbers and the operator

num1, operator, num2 = input('Enter Calculation: ').split()


# convert strings to integers
num1 = int(num1)
num2 = int(num2)


# provide output based on selected operator

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

else:
    print('Use either +, -, or * next time')

# print the result

print("{} {} {} = {}".format(num1, operator, num2, result))
