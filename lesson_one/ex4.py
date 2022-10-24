# We'll provide different output based on age
# 1 - 18 -> important
# 21, 50, -> Important
# All others -> Not Important


# Receive age and store in age
age = eval(input('Enter Age: '))



# if age is both greater than or equal to 1 and less than or equal to 18 Important

if (age >= 1) and (age <= 18):
    print('Important Birthday')

# if age is either 21 or 50 Important

elif (age == 21) or (age == 50):
    print('Important Birthday')


# check if age is less than 65 and then convert true or false and vice versa

elif not(age < 65):
    print('Important Birthday')

# Else Not Important

else:
    print('Not Important')
