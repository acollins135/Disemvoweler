# Creates a user input
input = input("Type a sentence: ")

#takes input and removes vowels
def remove_vowels(input):
    vowels = "aeiouAEIOU"
    for char in vowels:
        input = input.replace(char, "")
    return input

#prints the new input
print(remove_vowels(input))