class Game(): #the masterclass of game
    '''
    A Mater Class of game.
    '''
    def __init__(self, attempts):
        self.greeting = "Welcome to Play!"
        self.attempts=attempts
        self.player = None
        self.afterwords= "thanks for playing. See you again soon."

    def greet(self):
        self.player = input("Please Enter Your Name: ")
        print("Hello {}\n{}".format(self.player, self.greeting))

    def play(self):  #to be overwritten
        pass

    def epilogue(self):
        print("\n{}, {}".format(self.player, self.afterwords))
        input("Please click any key to exit.")
