import random

MAX_TRIALS = 100

tsp = [[0, 400, 500, 300],
       [400, 0, 300, 500],
       [500, 300, 0, 400],
       [300, 500, 400, 0]
       ]
cities = len(tsp)

def Value(state):
    # write your code here
    total = 0
    for i in range(len(state)):
        a = state[i]
        b = state[(i + 1) % len(state)]  # % wraps back to first city
        total += tsp[a][b]
    return total
def get_neighbor(state):
    # write your code here
    i, j = random.sample(range(cities), 2)
    neighbor = state[:]
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing(state):
    # write your code here
    current = state[:]
    current_val = Value(current)
    trials = 0
    while trials < MAX_TRIALS:
        neighbor = get_neighbor(current)
        v = Value(neighbor)

        if v < current_val:
            current = neighbor
            current_val = v
            trials = 0
        else:
            trials += 1

    return current

best_state = []
best_dist = 100000
for k in range(20):
    state = list(range(cities))
    random.shuffle(state)
    state = hill_climbing(state)
    v = Value(state)
    if best_dist > v:
        best_dist = v
        best_state = state
    
print(best_state, best_dist)
