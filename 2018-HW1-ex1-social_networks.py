
"""
<<<
	Problem 1. We create a small-world graph G according to the following model. We start with a
	directed cycle with n nodes. That is, we have nodes v1, v2, . . . vn and we have a directed edge from
	each vi to vi+1 (vn is connected to v1). Each of these edges has length 1. In addition there exists
	another “central” node v, which is connected to each of the nodes vi with probability p, each choice
	being mutually independent from all the other choices. Each edge (v, vi) that exists is undirected
	and has length 1/2. In other words, we create some shortcuts of length 1 between some pairs of
	nodes (those for which an edge exists).

		1. Consider two nodes vi, vj on the cycle, such that the distance from vi to vj on the cycle is k.
			Let P(l, k) be the probability that the shortest path between vi and vj is exactly l. Calculate P(l, k).
		
		2. Compute the distribution P(l) of the shortest path between the nodes on the cycle.
		
		3. Optional, bonus: Compute the average distance between the nodes on the graph. Assume that n is sufficiently large
>>>

Here I calculate analytically these probability and I plot their going 
"""

try:
	from matplotlib import pyplot as plt 
except ImportError:
	plt = None


N = 20
p = 0.5


def P_path(l,k):
	"""
	Probability that exists a generic path (doesn't need to be the shortest) of exactly length 'l'
	which cuts through the central node v
	"""
	if l>k:
		# For simplicity return 0
		return 0.0

	if l==k:
		# A path always exists
		return 1.0  

	return (2*l - 1) * (p**2) * ((1-p)**(l-1))



def P_exact(l,k):
	"""
	Probability that the shortest path between two nodes distanced 'k' in the ring has length exactly equal to 'l'.  
	It is equal to the product of the probabilities that a path shorter than 'l' doesn't exist {res *= 1 - P_path(d)}
	multiplied by the probability that a path with length 'l' exists
	"""
	if l>k:
		return 0.0
	P_no_smaller = 1.0

	for d in range(1,l):  #cycle from d=1 to d=l-1
		P_no_smaller *= 1 - P_path(d,k)

	#Here no path with length l-1 or lower exists. Return the result times the probability that exists a path of length 'l' 
	return P_no_smaller * P_path(l,k)



def P(l):
	"""
	Probability distribution of the nodes in the cycle.
	Average the probability P_exact('l','k') over all possible values of 'k', namely from 1 to n/2, max distance on the circle
	"""
	s = 0.0
	max_k = int(N/2)
	for k in range(1,max_k+1):
		s += P_exact(l,k)
	return s/max_k


def avg_distance():
	"""
	Expected value of the shortest path
	"""
	return sum([l*P(l) for l in range(int(N/2))])



k = 8
Ps = [P_exact(l, k) for l in range(1,N)]
print(f"Sum: {sum(Ps)}")
if plt:
	plt.scatter(range(1,N), Ps)
	plt.plot(range(1,N), Ps)
	plt.xlim(0), plt.ylim(0)
	plt.xticks(range(1,N))
	plt.title(f"$P\\_exact(l, k={k})$")
	plt.show()



Ps = [P(l) for l in range(1,N)]
print(f"Sum: {sum(Ps)}")
if plt:
	plt.scatter(range(1,N), Ps)
	plt.plot(range(1,N), Ps)
	plt.xlim(0), plt.ylim(0)
	plt.xticks(range(1,N))
	plt.title("$P(l)$")
	plt.show()


print(f"\n>>> Average distance between nodes with p={p}: {avg_distance():.2f}")
