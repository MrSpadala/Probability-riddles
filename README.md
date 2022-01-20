
## Probability riddles

Here I report solutions of some probability-related riddles and curiosities that I found around.

I solve them using an analytical solution, which can be in a closed or recursive form (recursive or iterative implemented with dynamic programming), and sometimes evaluate its correctness simulating the random process many times and obtaining the result.

---

 - [__match__](../master/match.py) - In this problem we have two same decks of cards. We extract simultaneously a card from both of
  the decks. If the cards happens to be the same (same number, same kind) we have a "match".
  If we extract all cards from the decks, it is more probable to have or not to have a match during the game?
  
    Spoiler: with 52 cards you have a match probability of 63%
 
 - [__ex1 social networks__](../master/2018-HW1-ex1-social_networks.py) - We create a small-world graph G according to the following model. We start with a
	directed cycle with n nodes. That is, we have nodes v1, v2, ... vn and we have a directed edge from
	each vi to vi+1 (vn is connected to v1). Each of these edges has length 1. In addition there exists
	another “central” node v, which is connected to each of the nodes vi with probability p, each choice
	being mutually independent from all the other choices. Each edge (v, vi) that exists is undirected
	and has length 1/2. In other words, we create some shortcuts of length 1 between some pairs of
	nodes (those for which an edge exists).
	  
    1. Consider two nodes vi, vj on the cycle, such that the distance from vi to vj on the cycle is k.
			Let P(l, k) be the probability that the shortest path between vi and vj is exactly l. Calculate P(l, k).
		
    2. Compute the distribution P(l) of the shortest path between the nodes on the cycle.
		
    3. Optional, bonus: Compute the average distance between the nodes on the graph. Assume that n is sufficiently large

 - [__hit__](../master/critical_hit.py) - This came up when reading [this](https://probablydance.com/2019/08/28/a-new-algorithm-for-controlled-randomness/) article on probablydance.com blog, found on hackernews. As the author states:
  
    <<< The description of the problem is this: An enemy is supposed to drop a crucial item 50% of the time.
    Players fight this enemy over and over again, and after fighting the enemy ten times the item still hasn’t dropped.
    They think the game is broken. Or an attack is supposed to succeed 90% of the time but misses three times in a row.
    Players will think the game is broken. >>> 
    
    
 - [__123 solitaire__](../master/123_solitaire.py) - In this game we have a deck of cards, our objective is to extract all cards from it.
We do this by extracting the first card from the top and yelling "One!", then extracting
the second and yelling "Two!", then the next one and yelling "Three!", then next one again
yelling "One!" and so on, screaming "One!", "Two!" or "Three!" in loop.
The rule of the game is that if we pick an ace when we yell "One!", a two when we say "Two!",
or a three when we say "Three!" the game is lost.
Which is the probabiliy of winning?   

    Spoiler: it is very low, with the italian deck (40 cards) you have 0.8307% winning chance  

 - [__observe all cards__](../master/observe_all.py) - Suppose having a card deck with M cards. Consider the following experiment: for N>=M times, pick a card, write it down and re-insert it in the deck.

    What is the probability that you observe all the M cards in the deck with N tries (or less)?
