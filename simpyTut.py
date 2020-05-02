```
This is simulation that simulates the path of a movie go-er

1. Arrives at the theater gets in line, waits to purchse ticket
2. Buys a ticket from the box office
3. waits in like to have ticket chekced
4. gets the ticket checked by usher
5. choses whether or not to get in line for the concession stand:
	- if they get in line, they purchase food
6. they go find their seat
```

import simpy
import random
import statistics

wait_times = []

class Theater(object):
	def __init__(self, env, num_cashiers, num_servers, num_ushers):
		self.env = env
		self.cashier = simpy.Resource(env, num_cashiers)
		self.server = simpy.Resource(env, num_servers)
		self.usher = simpy.Resource(env, num_ushers)
	
	def purchase_ticket(self, moviegoer):
		yield self.env.timeout(random.randint(1,3)) 

	def check_ticket(self, moviegoer):
		yeild self.env.timeout(3/60)

	def sell_food(self, moviegoer):
		yeild self.env.timeout(random.randint(1,5))

def go_to_movies()		

# Set up the environment
env = simpy.Environment()

# Assume you've defined checkpoint_run() beforehand
env.process(checkpoint_run(env, num_booths, check_time, passenger_arrival))

# Let's go!
env.run(until=10)



