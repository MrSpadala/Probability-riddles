
"""
This came up when reading this article https://probablydance.com/2019/08/28/a-new-algorithm-for-controlled-randomness/
found on hackernews. As he states:
<<<
	The description of the problem is this: An enemy is supposed to drop a crucial item 50% of the time.
	Players fight this enemy over and over again, and after fighting the enemy ten times the item still hasn’t dropped.
	They think the game is broken. Or an attack is supposed to succeed 90% of the time but misses three times in a row.
	Players will think the game is broken.
>>>

And again, the idea of his solution that it is also used in Warcraft 3:
<<<
	The idea is that you keep on increasing the chance every time that something fails to happen.
	Let’s say you have a 19% chance to get a critical hit. Then the first time you attack, 
	and you want to calculate if it was a critical hit or not, you use true randomness with a 5% chance of succeeding.
	If you don’t land a critical hit, the next time you will get a 10% chance. If you fail again your chance goes up to 15%,
	then 20%, 25% etc. If you keep on failing, at some point you will have a 100% chance of landing a critical attack.
	But if you succeed at any point, your chance goes back down to 5%.
>>>


What I wanted to do is to find the probability distribution of hitting the target over the number of tries
and the mean probability to hit, gived the start probability and its increase at every step (at every missed hit)


I perform the following steps:
	1.  I start by finding the probability distribution to score a hit over the number of tries,
	or, in other words, to analytically find the probability to score a hit at the n-th try, for all possible values of n. 

	2.  Take the expected number of tries given the probability values calculated above

	3.  The average probability to score a hit is given by the inverse of the expected number of tries
"""



from pprint import pprint
import numpy as np
import random
random.seed(42)

try:
	from matplotlib import pyplot as plt 
except ImportError:
	plt = None



# The first value of hit probability. Whenever a hit is scored, hit probability resets here
P_START = 0.05
# How much the hit probability is increased when missing a hit
P_INC = 0.05


def get_probabilities():
	# Returns a vector P for the probability P(try AND hit),
	# where P[i] = P(try=i AND hit), aka the probability to
	# be in the i-eth try and to score a hit
	# (too lazy to write efficient code)
	P = [P_START]
	n_increments = 0
	while True:
		n_increments += 1
		res = min(1.0, P_START + n_increments*P_INC)  #Probability to score in this try
		for i in range(n_increments):    
			res *= 1.0 - min(1.0, P_START + i*P_INC)  #Probability to not have scored in the previous tries
		if res <= 0:
			break
		P.append(res)
	return P


def expected_val(P):
	# Return expected value of probability vector P.
	# (i+1) to start the enumeration from 1
	return sum([(i+1)*P[i] for i in range(len(P))]) 

	


def get_hit_prob(verbose=True):

	P = get_probabilities()
	exp = expected_val(P)
	hit_prob = 1/exp

	if verbose:
		print("\n===============================")
		for i in range(len(P)):
			print(f"P(try={i+1} AND hit) = {P[i]:.8f}")
		print("===============================\n")

		if plt:
			plt.plot(range(len(P)), P)
			plt.scatter(range(len(P)), P)
			plt.show()
		else:
			print("[x] No plot, matplotlib missing\n")

		print(f">>> Expected number of tries to score a hit: {exp:.4f}")
		print(f">>> Mean probability to hit 1/{exp:.4f} = {hit_prob:.6f}\n")

	return hit_prob



def get_inc_prob(p_target):
	global P_INC, P_START
	min_err = 1.0
	step = 0.001
	for p in np.arange(step, p_target, step):
		P_INC = p
		P_START = p
		calc_p = get_hit_prob(verbose=False)
		if abs(calc_p-p_target) < min_err:
			min_err = abs(calc_p-p_target)
			best = p
	print(best)
	return best








def simulate():
	# Simulate the game and print the evaluated probability,
	# to compare to the one found analytically
	hits, steps = 0, 0
	p = P_START
	while hits < 10**6:
		if random.random() >= p:
			p += P_INC
		else:
			hits += 1
			p = P_START
		steps += 1
	print(f"[*] Simulated hit probability: {hits/steps:.6f}")	




if __name__ == '__main__':
	#get_inc_prob(0.1)
	get_hit_prob()
	simulate()




# - - trash not used - -

def P_comulative(p, step):
	if step <= 0:
		return 0.0
	if p >= 1.0:
		return 1.0
	return p + (1-p)*P(p+P_INC, step-1)