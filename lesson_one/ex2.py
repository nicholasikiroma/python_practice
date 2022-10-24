# Ask the user to input 2 values and store them in variables num1 num2

num1, num2 = input('Enter 2 numbers: ').split()

# convert the strings into regular number integar
num1 = int(num1)
num2 = int(num2)

# add the values and store in sum

sum1 = num1 + num2

# subtract the values and store in difference

difference = num1 - num2

# multiply the values and store in product 

product = num1 * num2
# divide the values and store in quotient

quotient = num1 / num2
# use modulus

remainder = num1 % num2 

# print results

print("{} + {} = {}".format(num1, num2, sum1))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

