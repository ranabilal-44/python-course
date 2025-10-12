word = input("Enter a word or number: ")

if word == word[::-1]:
    print(word, "is a palindrome ")
else:
    print(word, "is not a palindrome ")
