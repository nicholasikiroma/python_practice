# Problem: Encrypt Messages Using Ceaser's Cypher

# How it works: Parse a message that you want to be encrypted. Encryption is done by shifting them a certain amount. E.g. A = D, B = E


# Get message
msg = input("Enter your secret message: ")
key = int(input("Enter the number of characters to shift(1 - 10): "))

# Iterate through the message
for i in msg:

    if ord(i) in range(ord('A'), ord('Z') + 1) or ord(i) in range(ord('a'), ord('z') + 1):
        print(chr(ord(i) + key), end="")
print()
