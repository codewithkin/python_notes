#Problem statement: Write a Python program that takes a string as input and outputs the number of vowels in the string.

def countVowels(s):
    vowelsNumber = 0
    
    for character in s:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            vowelsNumber += 1
    
    return "There are " + str(vowelsNumber) + " vowels in " + s

print(countVowels("Kin"))