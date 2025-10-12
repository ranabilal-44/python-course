phrase = "Hey This is Just a String"
print(phrase.upper()) # to convert string in uppercase
print(phrase.lower()) # to convert string in lowercase
print(phrase.lower().islower()) # to check if string is in lowercase or uppercase
print(len(phrase)) # to check length of a string
print(phrase[0]) # to get character of specific index
print(phrase.index('Just')) # to get index of a specific character
print(phrase.replace("String", "Character")) # to replace any word or letter in a string
print(phrase.split())   # Output: ['Hey', 'This', 'is', 'Just', 'a', 'String']
print(phrase.count("i"))   # Output: 3
print(phrase.title()) # to capital 1st letter of evey single world
print(phrase.center(40, '-'))  # Centers the string within a width of 40 using '-'
print(phrase.endswith("a"))  # Checks if string ends with given word → True
