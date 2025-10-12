def swap_case(phrase):
    result = ""  
    for letter in phrase:  
        if letter.isupper():    
            result = result + letter.lower()   
        elif letter.islower(): 
            result = result + letter.upper()  
        else:  
            result = result + letter   
    return result

print(swap_case(input("Enter your phrase: ")))
