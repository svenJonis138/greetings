def camelCase():
    # greets our user with a lovely banner
    def banner():
        """Display welcome banner"""
        message = "CAMELCASE PROGRAM!!"
        stars = '*' * len(message)
        print(f'{stars}\n{message}\n{stars}')
    banner()
    # explains how this next-level program will work
    def instructions():
        print("All you have to do is type in any sentence and this handy program will convert it to camelCase homie!")
        print("No more sleepless nights trying to convert your meaningful variable names into camelCase!")
    instructions()

    # takes the users input to convert to camelCase
    newVariable = input("What is the name you would like to convert to camelCase? ")

    # checks to see if new var name is valid
    if not newVariable[0].isalpha():
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


