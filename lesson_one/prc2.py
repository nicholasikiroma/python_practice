# if age is 5 Go to kindergarten

# ages 6 through 17 goes to grades 1 through 12


# if age is greater than 17 say go to college

# try to complete with 10 or less lines


# receive and store input in age

age = int(input("Enter your age: "))

# check if age with range 6-17
if age == 5:
    print("Go to kindergarten")

elif (age >= 6) and (age <= 17):
    print("Ages 6 through 16 goes to grades 1 through 12")


elif (age > 17):
    print("Go to college")

else:
    print("Not old enough")
