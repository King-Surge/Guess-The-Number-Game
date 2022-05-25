log = print

GUESS = 90

guess = ""

if guess != GUESS:
    
    guess = int(input("Try And Get The Correct Number \n Enter A Number: "))
    
    if guess <= 50:
        log("That number is way too small")
    elif guess >= 51 and guess <= 89:
        log("Your Getting A Bit Closer")
    elif guess >= 91 and guess <= 101:
        log("I guess your a bit closer and higher")
    elif guess >= 102:
        log("That Number is way too big")
    
if guess != GUESS:
    
    guess = int(input("Try And Get The Correct Number \n Enter A Number: "))
    
    if guess <= 50:
        log("That number is way too small")
    elif guess >= 51 and guess <= 89:
        log("Your Getting A Bit Closer")
    elif guess >= 91 and guess <= 101:
        log("I guess your a bit closer and higher")
    elif guess >= 102:
        log("That Number is way too big")
    
if guess != GUESS:
    
    guess = int(input("Try And Get The Correct Number \n Enter A Number: "))
    
    if guess <= 50:
        log("That number is way too small")
        log("Sorry Out Of Attempts. The Number Was " + str(GUESS))
    elif guess >= 51 and guess <= 89:
        log("Your Getting A Bit Closer and higher")
        log("Sorry Out Of Attempts. The Number Was " + str(GUESS))
    elif guess >= 91 and guess <= 101:
        log("I guess your a bit closer")
        log("Sorry Out Of Attempts. The Number Was " + str(GUESS))
    elif guess >= 102:
        log("That Number is way too big")
        log("Sorry Out Of Attempts. The Number Was " + str(GUESS))
        

    
if guess == GUESS:
    log("Congrats The Number was " + str(GUESS))
