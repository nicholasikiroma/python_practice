msg = input("Enter message: ")

# iterate through input string
for i in msg:

# check for upper and lower case characters
    if ord(i) in range(ord('a'), ord('z') + 1) or ord(i) in range(ord('A'), ord('Z') + 1):

# print ascii equivalent of string
        print(ord(i), end="")
print()

print("original message is: ", msg)
