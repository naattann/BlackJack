import random

print("Python Casino!\n")
tokens = int(input("How many tokens do u want to buy?: "))


def __init__():

	global deck
	
	if input("\n1: Play   2: Quit : ") == "1":		
		deck = ["2","3", "4", "5"," 6"," 7","8", "9", "10", 'J', 'Q', 'K', 'A']
		deck=  [card for card in deck for i in range(4)]		
		deck = random.sample(deck,len(deck))
		loop()		
	else:
		print("Closing")
		exit(0)

def hit(hand):
	card = deck.pop()
	hand.append(card)
	return hand

def score(hand):

	score = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			score+= 10
		elif card == "A":
			if score >= 11:
				score+= 1
			else:
				score+= 11
		else:
			score += int(card)
	return score

def blackjack_lose(dealer_hand, player_hand):

	global tokens, bid

	if score(player_hand) == 21:
		print("\nYou got a Blackjack! "+ str(player_hand))
		tokens += bid
		__init__()

	elif score(dealer_hand) == 21:
		print("\nThe dealer got a Blackjack! "+ str(dealer_hand))
		tokens -= bid
		__init__()

	elif score(player_hand) > 21:
		print("\nYou busted. You lose"+ str(player_hand))
		tokens -= bid
		__init__()

	elif score(dealer_hand) > 21:
		print("\nDealer busts. You win!" +str(dealer_hand))
		tokens += bid
		__init__()

def check_winner(dealer_hand, player_hand):

	global tokens, bid
	
	print("The dealer deck " + str(dealer_hand) + " Yours deck" + str(player_hand))	

	if score(player_hand) < score(dealer_hand):	
		print("\nDealer score is higher. You lose.\n")
		tokens -= bid
	elif score(player_hand) > score(dealer_hand):					   
		print("\nYour score is higher. You win\n")
		tokens += bid
	else:
		print("Draw!\n")
			

def loop():

	global deck, tokens,bid
	dealer_hand = []
	player_hand = []
	dealer_hand = hit(hit(dealer_hand))
	player_hand = hit(player_hand)
	print("\nThe new round has been started\n")
	print("\nYou have "+ str(tokens)+ " tokens left\n")

	if tokens == 0:
		tokens = int(input(("\nYou do not have tokens, how many more want you to buy?: ")))
	bid = int(input("\nType your bid: "))

	while bid > tokens:
		bid = int(input(("\nYou do not have enough tokens specify other amount: ")))


	while True:
		print("\nThe dealer is showing a " +str(dealer_hand[0]))
		print("You have a " +str(player_hand))
		blackjack_lose(dealer_hand, player_hand)
				
		if input("\n1: Hit    2: Stand : ") == "1":
			hit(player_hand)
			if score(dealer_hand) < 17:
				hit(dealer_hand)
			elif score(dealer_hand) >= 17:
				print("Dealer Stands")
			blackjack_lose(dealer_hand, player_hand)
			
		else:
			while score(dealer_hand) < 17:
				hit(dealer_hand)
			check_winner(dealer_hand, player_hand)
			__init__()


__init__()			
if __name__ == "__main__":
   loop()
