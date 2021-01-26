def camelCase():

    # takes the users input to convert to camelCase
    newVariable = input("What is the name you would like to convert to camelCase? ")

    # checks to see if new var name is valid
    if newVariable[0].isalpha() == False :
        # if not valid, prints an error message and ends program
        print("Warning, you cannot name a variable with the first char as a number or symbol ")
        # if valid, converts to camel case
    else:
        # takes given sentence and splits up words
        words = newVariable.split()
        # creates a list to hold words
        wordsCap = []
        # for each loop to run through words
        for word in words:
            # adds words to list and capitalizes first letter
            wordsCap.append(word.title())
        # joins all words into a string and removes space
        camelCase = ''.join(wordsCap)
        # now takes the first letter and turns it to lowercase
        newWord = camelCase[0].lower() + camelCase[1:]
        print("Your variable name is " + str(newWord))

camelCase()