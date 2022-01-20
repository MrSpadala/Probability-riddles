"""
Suppose having a card deck with M cards. Consider the following experiment:
for N>=M times, pick a card, write it down and re-insert it in the deck.
What is the probability that you observe all the M cards in the deck with N tries?
"""
import numpy as np

N = 200
M = 52

def compute(N,M):
	# Initialize matrix with size N+1, M+1 all elements -1.
	# mat[i,j] is the probability of seeing M-j elements with i tries
	mat = np.zeros((N+1,M+1)) - 1.0

	# Iterations on all n,v elements of the matrix.
	# The iteration on the matrix is done so that elements considered for the computation
	# are already computed and stored in the matrix
	for n in range(N+1):
		for m in reversed(range(M+1)):
			if n < M-m:
				mat[n,m] = 0.0
			elif m >= M:
				mat[n,m] = 1.0
			else:
				# Calculate probability of observing an unseen element
				p_new = (M-m)/M
				# Update the matrix
				mat[n,m] = p_new * mat[n-1,m+1] + (1-p_new) * mat[n-1,m]
	return mat[N,0]


print(f"Probability of observing all {M} cards with {N} tries:")
print(">>>", compute(N,M))


# Plot stuff, optional
try:
	import matplotlib.pyplot as plt
	from tqdm import tqdm
	x = list(range(1, 1000, 5))
	y = [compute(i, M) for i in tqdm(x, desc="Plotting...")]
	plt.xlabel("N"); plt.ylabel("Prob.")
	plt.plot(x,y)
	plt.show()
except ImportError:
	print("No matplotlib and/or tqdm found. Skip plot")
