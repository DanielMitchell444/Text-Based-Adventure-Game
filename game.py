def introScene():
    instructions = ["1", "2", "3"]
    print('You are playing video games with your younger brother, and he is currently winning, what do you want to do?')
    userInput = ""

    while userInput not in instructions:
     print("Options: 1, 2, 3, 4")
     userInput = input()
     if userInput == "1":
        showAction()
     elif userInput == "2":
        scream()
     elif userInput == "3":
        throw()
     elif userInput == "4":
        print('You find the wall doesnt wrk')
     else:
        print('Please select an option using numbers 1,2, and 3')

def scream():
    instructions = ["1", "2", "3"]
    print('You scream at the top of your lungs, shutting your brother up and waking up your mom. Your mom wakes up and opens the door, and starts walking towards you. What do you do?')
    userInput = ""
    print("1: Pretend to go to bed to decieve your mom, 2: Wait until your mom comes to you 3: Continue playing")
    while userInput not in instructions:
     userInput = input()
     if userInput == "1":
        decieve()
     elif userInput == "2":
        wait()
     elif userInput == "3":
        continuePlaying()
     else:
        print('Please select an option using numebrs 1,2, and 3')

def showAction():
    instructions = ["1:Put your hand over his mouth", "2: STAB HIM!", "3: Let him cry "]
    print('You hit him and he starts to cry, and starts screaming for mom while jumping up and down. What do you do?')
    userInput = ""
    print('1: Put your hand over his mouth 2: STAB HIM!, 3: Let him cry ')
    while userInput not in instructions:
     userInput = input()
     if(userInput == "1"):
        mouth()
     elif userInput == "2":
        stab()
     elif userInput == "3":
        cry()
     else:
        print('Please select an option using numbers 1, 2, and 3')
    


if __name__ == "__main__":
   while True:
    print('Welcome to the game')
    print('You are an avid traveller, you decide to visit the meme shop')
    print('However, during your adventure, you find yourself lost')
    print('You can choose to walk multiple directions')
    print('lets start with your name')
    name = input()
    print('Goodluck, ' + name + ".")
    introScene()

