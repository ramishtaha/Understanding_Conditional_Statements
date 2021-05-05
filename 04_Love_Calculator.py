print("Welcome to The Love Calculator!!!\n")
# Use String.lower() function to change the String to lowercase.
name1 = input("What is your name? ").lower()
name2 = input("What is their's name? ").lower()

# true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

# love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

# I did code the above lines but I think the lower ones are better.

# Concatenate both the names.
name = name1 + name2

# Use String.count() function to count the number of occurrences of a certain string.
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

# Concatenate both the Scores one after another.
true_love = int(str(true) + str(love))

# Use if statement to print out what type of love they have.
if true_love < 10 or true_love > 90:
    print(f"Your Score is {true_love}, You go together like coke and mentos.")
elif 45 < true_love < 55:
    print(f"Your Score is {true_love}, You are Alright There")
else:
    print(f"Your Score is {true_love}")
