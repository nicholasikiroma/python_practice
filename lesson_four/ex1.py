rand_string = "     this is an important string   "

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

o_list = ["Bunch", "of", "random", "words"]
print(" ".join(o_list))

print("how many is: ", rand_string.count("is"))

print(rand_string.replace("an ", "a kind of "))
