## King Markov's Island-Hopping Adventure
# Python adaptation of R code, pg 243 of Statistical Rethinking by Richard McElreath
# Love, Laura.

import numpy as np # Lets us easily work with arrays
import matplotlib.pyplot as plt # Lets us plot our data
plt.style.use('solarize') # This stuff is just to make the plots look pretty online.

# By default, we run over a year (52 weeks) and the title of the resulting graph will reflect that.
def metropolis(numWeeks = 52, title = "Visits over One Year"):
	positions = np.zeros(numWeeks) # Right now, the king hasn't been anywhere, so the record of his positions is a whole bunch of 0's.
	current = 10. # The king is currently on island 10.
	hT = np.array([-1, 1]) # A coin. -1 = tails, 1 = heads

	for i in range(1, numWeeks): # Each week...
		print("Week #", i)
		positions[i] = current # The king is where he is right now
		proposal = current + hT[np.random.randint(0, 2)] # flip the coin. 
		# This if/elif statement just lets us loop around from island 10 to island 1 if we have to.
		if proposal < 1.:
			proposal = 10.
		elif proposal > 10.:
			proposal = 1.
		probMove = proposal/current # Pull out our shells and stones
		decisionBag = np.random.ranf() # Load our decision bag
		if decisionBag < float(probMove): # If we should move ... 
			current = proposal # ... then move!
	# And now we'll just plot that out! 
	plt.hist(positions, edgecolor='#002b36', linewidth=1.2)
	plt.xlabel('Island')
	plt.ylabel('Times Visited')
	plt.title(title)
	plt.show()
	plt.savefig(str(numWeeks) + '_weeks.png', facecolor='#002b36')

metropolis() # Let King Markov travel for one year
metropolis(52000, "Visits over One Millenium") # Let King Markov travel for 1000 years.

