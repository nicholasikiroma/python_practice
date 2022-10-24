def ceaser_cypher(message, key):
    """
    Encrypts string of text using Ceaser Cypher

    """
    secret_message = ""

    for char in message:

# check if char is alphabet
        if char.isalpha():

            char_code = ord(char)
            char_code += key

            if char.isupper():

# Handle cases where shifting exceeds character range
                if char_code > ord('Z'):
                    char_code -= 26

                if char_code < ord('A'):
                    char_code += 26

            else:

                if char_code > ord('z'):
                    char_code -= 26

                if char_code < ord('a'):
                    char_code += 26

            secret_message += chr(char_code)

# print spaces, tabs and other characters
        else:
            secret_message += char

    return secret_message


def decrypt_ceaser(encrypted_msg, key):

# Decrypt


    key = -key
    msg = ""
    for i in encrypted_msg:

        if i.isalpha():

            chars = ord(i)
            chars += key

            if i.isupper():
                if chars > ord('Z'):
                    chars -= 26

                if chars < ord('A'):
                    chars += 26

            else:

                if chars > ord('z'):
                    chars -= 26

                if chars < ord('a'):
                    chars += 26

            msg += chr(chars)

        else:
            msg += i
    return msg


msg = input("Enter your secret message: ")
key = int(input("Input Ceaser's key: "))
encrypt = ceaser_cypher(msg, key)
print("Your encrypted message is:", encrypt)

decrypt = decrypt_ceaser(encrypt, key)

print("Your original message is:", decrypt)
