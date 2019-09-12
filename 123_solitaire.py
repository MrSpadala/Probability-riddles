
"""
In this game we have a deck of cards, our objective is to extract all cards from it.
We do this by extracting the first card from the top and yelling "One!", then extracting
the second and yelling "Two!", then the next one and yelling "Three!", then next one again
yelling "One!" and so on, screaming "One!", "Two!" or "Three!" in loop.

The rule of the game is that if we pick an ace when we yell "One!", a two when we say "Two!",
or a three when we say "Three!" the game is lost.

Which is the probabiliy of winning?   


Spoiler: it is very low, with the italian deck (40 cards) you have 0.8307% winning chance  
"""


import numpy as np
from math import ceil


N = 40  	#total number of cards
KINDS = 4  	#how many kinds of cards
assert(not N%KINDS)


# Initialize dynamic progr. matrix to all negative entries
#
# example: M[n][X][Y][Z] probability of winning the game when we have n cards left
# 	and in the deck there are X ones, Y twos and Z threes
M = np.zeros(shape=(N+1,KINDS+1,KINDS+1,KINDS+1)) - 1.0



def P(n,X,Y,Z):
	"""
	Returns the probability to win the game with n cards in 
	the deck and X ones, Y twos and Z threes left in the deck
	"""

	# Check if state has already been calculated
	if M[n][X][Y][Z] >= 0.0:
		return M[n][X][Y][Z]

	# If the deck is empty or all ones, all twos and all threes have been picked up, the game is won
	if n==0 or (X==0 and Y==0 and Z==0):
		return 1.0

	# Probability to win in the follow up game
	win_prob = 0

	# Add probability to pick nor a one, nor two nor three, times the probability of winning the game with n-1 cards.
	# It is >0, not >=0, since if n-X-Y-Z==0 there aren't cards other than 1s, 2s or 3s
	if n-X-Y-Z > 0:
		win_prob += ((n-X-Y-Z)/n) * P(n-1,X,Y,Z)

	# Add probability (X/n) to pick a one (only if I am not saying "one" during the peek numbered N-n)
	# times the probability of winning the game with n-1 cards and X-1 ones left in the deck
	if X > 0 and not ((N-n)%3 == 0):
		win_prob += (X/n) * P(n-1,X-1,Y,Z)

	# Same as before but with the two
	if Y > 0 and not ((N-n)%3 == 1):
		win_prob += (Y/n) * P(n-1,X,Y-1,Z)

	# Same as before but with the three
	if Z > 0 and not ((N-n)%3 == 2):
		win_prob += (Z/n) * P(n-1,X,Y,Z-1)

	# Update the value in the matrix
	M[n][X][Y][Z] = win_prob
	return win_prob


def get_win_prob():
	return P(N, KINDS, KINDS, KINDS)



def simulate():
	"""
	Performs some random games to simulate the winning probability found analytically
	"""
	np.random.seed(42)
	mask = np.asarray([1,2,3]*ceil(N/3))[:N]
	won, lost = 0, 0
	for i in range(10**6):
		deck = np.asarray(list(range(1,int(N/KINDS)+1))*4)
		np.random.shuffle(deck)
		res = not any(deck == mask)
		if res:	won += 1
		else:	lost += 1
		
		if not i%10**4:
			p_eval = won/(won+lost)
			print(f">>> Simulated win probability with {i} games: {100*p_eval:.4f}%")




if __name__ == '__main__':
	p_win = get_win_prob()
	print(f">>>\n>>> Calculated win probability: {100*p_win:.4f}%\n>>>")


	def n_tries(P_target):
		P, i = 0, 1
		while P < P_target:
			P = 1-((1-p_win)**i)
			i += 1
		return i

	print(f">>> Number of tries to do for winning at least once with 90% confidency: {n_tries(0.90)}")
	print(f">>> Number of tries to do for winning at least once with 99% confidency: {n_tries(0.99)}\n>>>")

	simulate()

