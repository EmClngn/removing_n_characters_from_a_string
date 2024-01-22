# Write a program to remove characters from a string starting from zero up to n and return a new string.



# Pseudo Code

# asking users for a string and int respectively
string = input("What is your desried word?: ")
number_of_characters = int(input("What's the number of characters you want to be removed in the string? "))
string_length = len(string)

# write the program that will remove the chracters from the string
for i in range(number_of_characters, string_length):
    print(string[i])
