import guess_number_game

def main():
	guessnumber = guess_number_game.GuessNumberGame(5)
	guessnumber.greet()
	guessnumber.play()
	guessnumber.epilogue()

if __name__ == '__main__':
	main()

