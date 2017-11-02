import random
import game

class GuessNumberGame(game.Game): #subclass of Game
    '''
    Guess My Number Game -- A Game in which the player provides a number and the computer guess it. 
    '''
    def __init__(self, attempts):
        super(GuessNumberGame, self).__init__(attempts)
        self.greeting = "You, the player, are thinking of a number between 1 and 100.\n\
I, the clever computer will try to guess it in as few \n\
attempts as possible. I have {} attempts.".format(self.attempts)

    
    def play(self):
    	theNumber = int(input("\nThink of a number: "))

    	# Computer makes a first guess
    	attNum = 0

    	# Setting the range the machine can guess numbers from
    	low = 1
    	high = 100

    	# has the machine won yet?
    	win = False

    	# The computer gets five guesses
    	while attNum < self.attempts:
   
    		guess = random.randint(low,high)
    		attNum += 1
    		outcome = input("\nIs it {} (Yes, Higher, Lower): ".format(guess))
    	

    		if (outcome == 'Yes' and guess == theNumber):
    			win = True
    			break

    		elif(outcome == 'Higher' and guess < theNumber):
    			low = guess+1

    		elif(outcome == 'Lower' and guess > theNumber):
    			high = guess-1

    		else:
    			attNum -= 1
    			print("\nYou gave me a invalid response. Please play fair.")
    			print("I will make a new guess (and i still have {} attempt(s) left.\n".format(self.attempts - attNum))
    	if (win):
    		print("Yes! I told you I am clever! The number is {}".format(guess))
    	else:
    		print("Arrrgh, you beat me.")

    pass         

