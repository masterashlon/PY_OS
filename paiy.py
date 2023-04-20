#simple ai to interact for now with trivial tasks such as a game, google and amazon search
import webbrowser
from random import randint

URL_GOOGLE = "https://www.google.com/search?q="
URL_AMAZON = "https://www.amazon.com/s?k="

def amazon_search(search_word):
	search_word_list = search_word.split(" ") # for now conside the first word as the key for undestand that it can be a product name that user want to buy
	#print(search_word_list)
	if len(search_word_list) > 1:
		search_word_list.pop(0)
		#print(search_word_list)
		webbrowser.open(URL_AMAZON + " ".join(search_word_list)) # join the list of words except the first to make a search word
		print("\tA page with amazon search is opened for you \U0001F60C")

	else:
		print("\twhat? nothing?! OK \U0001F928")


def play_with_paiy(): #simple game : guess the random number
	random_value = 1#randint(1,3)
	if random_value == 1:
		print("\tWelcome to: Guess the number!\n\tI'm thinking of a number between 1 and 10(only integer).\n\tTake a guess.")

		score = 10
		max_number = 10
		min_number = 1
		secret_number = randint(min_number, max_number)
  
		print("Good luck! \U0001F638")
		while(True):
			inserted_number = int(input("\t--> "))
			if(inserted_number == secret_number):
				print("\tYou guessed it!")
				break
			if(inserted_number > secret_number):
				print("\tTry a bit less!")
				if(score > 0):
					score -= 1
			if(inserted_number < secret_number):
				print("\tTry a bit more!")
				if(score > 0):
					score -= 1
			print("\tYou have " + str(score) + " points left!")

		print(f"\n\tThanks for playing with me!\n\tYour score is: {score}")


def dialog_with_paiy():

	random_value = randint(1,5) # value to be random the welcome message

	if random_value == 1:
		paiy_salut = "Hiii \U0001F643"
	elif random_value == 2:
		paiy_salut = "Hello! \U0001F642"
	elif random_value == 3:
		paiy_salut = "Hey wazupp buddy \U0001F61C"
	elif random_value == 4:
		paiy_salut = "Oh \U0001F633 . I'm not waiting anyone right now \U0001F62C\n\tHowever, I'm glad to see you \U0001F60F"
	elif random_value == 5:
		paiy_salut = "WOW! A Human \U0001F632\n\tCan i help you? \U0001F9D0"

	print(f"\n\t{paiy_salut}\n\tPaiY is here for you \U0001F60A\n\tI' m a AI that can assist you with different things \U0001F60E")

	bool_condition = True
	while(bool_condition):
		
		paiy_command = str(input("\n\t-->")).strip().lower() # remove the white spaces and convert to lower case so it's similar to os terminal
		if paiy_command != "":
			
			if paiy_command == "bye" or paiy_command == "bye bye" or paiy_command == "see u" or paiy_command == "see you" or paiy_command == "see you next time" or paiy_command == "i have to go" or paiy_command == "close" or paiy_command == "exit" or paiy_command == "finish" or paiy_command == "end":
				print("\n\tI am here if you need my help again \U0001F609. GoodBye! \U0001F917\n")
				bool_condition = False
				break
			elif "need" in paiy_command or "want" in paiy_command or "buy" in paiy_command or "wish" in paiy_command:
				amazon_search(paiy_command)

			elif "game" in paiy_command or "play" in paiy_command:
				play_with_paiy()
				
			else:
				webbrowser.open(URL_GOOGLE + paiy_command)
				print("\n\tSorry if I don't understand \U0001F62B.\n\tMy Father \U0001F9D4 adds new feature constantly to improve my ability and help you for thousands and more questions and i will became more useful soon \U0001F97A.\n\tHowever a google search can help you, i guess \U0001F615\n")
		else:
			continue