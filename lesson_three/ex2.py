# Problem: Program that converts a string to ascii values

# A - Z = 65 - 90
# a - z = 97 - 122


# Get string from user

msg = input("Kindly Enter Your Message: ")


secret_msg = ""
# Iterate through string, print ascii values
for char in msg:

    secret_msg += str(ord(char) - 23)

print("Secret message is: ", secret_msg)

msg = ""
for i in range(0, len(secret_msg) -1, 2):

    char_code = secret_msg[i] + secret_msg[i+1]

    msg += chr(int(char_code) + 23)

print("Original Message is: ", msg)
