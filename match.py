
"""
In this problem we have two same decks of cards. We extract simultaneously a card from both of
the decks. If the cards happens to be the same (same number, same kind) we have a "match".

If we extract all cards from the decks, it is more probable to have or not to have a match during the game?


Spoiler: with 52 cards you have a match probability of 63%
"""


import numpy as np

N = 52  #number of cards


# Dynamic progr. matrix for function P
M = np.zeros(shape=(N+1,N+1)) - 1.0 


def P(n, n_same_cards):
	"""
	Probability to get a match having 'n' cards in both of the decks and 'n_same_cards'
	number of cards which are the same
	"""
	if n==0 or n_same_cards==0:
		return 0.0

	if M[n][n_same_cards] >= 0:
		return M[n][n_same_cards]

	# Probability to have a match in this turn
	p_match = ((n_same_cards/n)**2) * (1/n_same_cards)

	# Probability that _only one_ extracted card is common between the two decks
	#times the probability of winning the game in future turns (with n-1 cards and one card less in common)  
	p_match += P(n-1, n_same_cards-1) * 2*(n_same_cards/n)*(1-n_same_cards/n) 

	# Probability that _both_ extracted cards are common between the two decks (but they are different)
	#times the probability of winning the game in future turns (with n-1 cards and two card less in common)  
	if n_same_cards > 1:
		p_match += P(n-1, n_same_cards-2) * ((n_same_cards/n)**2) * (1-1/n_same_cards)

	# Probability that _no_ extracted card is common between the two decks
	#times the probability of winning the game in future turns (with n-1 cards and the same cards in common)  
	if n >= n_same_cards+1:
		p_match += P(n-1, n_same_cards) * ((1-n_same_cards/n)**2)

	M[n][n_same_cards] = p_match

	return p_match



def simulate():
	"""
	Simulate games and obtain match probability
	"""
	np.random.seed(42)
	won, lost = 0, 0
	for i in range(10**6):
		deck1, deck2 = np.arange(N), np.arange(N)
		np.random.shuffle(deck1)
		np.random.shuffle(deck2)

		res = any(deck1 == deck2)
		if res:	won += 1
		else:	lost += 1		

		if i and not i%10**4:
			print(f">>> Simulated match probability: {100*won/(won+lost):.2f}%")




if __name__ == '__main__':
	print(f"\n>>> Calculated match probability: {100*P(N, N):.2f}%\n")
	simulate()





