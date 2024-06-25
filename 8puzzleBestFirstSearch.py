# 8 puzzle best first search

from queue import PriorityQueue

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])

# The range(0, 9, 3) generates numbers 0, 3, 6.

# start = 0: The sequence starts at 0.
# stop = 9: The sequence stops before reaching 9.
# step = 3: The sequence increments by 3 each time.

# First Iteration (i = 0): state[0:3] prints the first row (index 0 to 2).
# Second Iteration (i = 3): state[3:6] prints the second row (index 3 to 5).
# Third Iteration (i = 6): state[6:9] prints the third row (index 6 to 8).

# state[i:i + 3] is a slicing operation on the tuple or list state.
# It extracts a sublist from state starting from index i (inclusive) up to index i + 3 (exclusive).

# def heuristic(state, goal_state):
#     return sum(1 for i in range(9) if state[i] != goal_state[i])

def heuristic(state, goal_state):

    mismatch_count = 0

    for i in range(9):
        if state[i] != goal_state[i]:
            mismatch_count += 1

    return mismatch_count

def move(state, direction):

    blank_index = state.index(0) #This line finds the position of the blank tile (the tile with value 0) in the current state. The position is stored in blank_index.
    new_state = list(state) #Since tuples are immutable in Python, state is converted to a list called new_state to allow modifications.

    if direction == 'up' and blank_index > 2:
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]

    elif direction == 'down' and blank_index < 6:
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]

    elif direction == 'left' and blank_index % 3 != 0:
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]

    elif direction == 'right' and blank_index % 3 != 2:
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        
    else:
        return None
    
    return tuple(new_state)

def generate_neighbors(state):

    neighbors = []
    directions = ['up', 'down', 'left', 'right']

    for direction in directions:
        neighbor = move(state, direction)

        if neighbor is not None:
            neighbors.append(neighbor)

    return neighbors

def solve_puzzle(initial_state, goal_state, max_steps=10):

# Initialization
    current_state = initial_state
    current_cost = heuristic(initial_state, goal_state)
    steps = 0
    path = [current_state]

    print_state(current_state)
    print("Current heuristic : ",current_cost)
    print()

    priority_queue = PriorityQueue()
    priority_queue.put((current_cost, current_state)) #It inserts a new item into the priority queue.
    
    while not priority_queue.empty() and steps < max_steps:

        current_cost, current_state = priority_queue.get() #It retrieves and removes the item with the lowest priority (smallest value) from the priority queue.
       
        if current_cost == 0:
            print_state(current_state)
            print("Current heuristic : ",current_cost)
            print()
            print("Goal state reached!")
            break
        
        neighbors = generate_neighbors(current_state)

        for neighbor in neighbors:
            neighbor_cost = heuristic(neighbor, goal_state)
            priority_queue.put((neighbor_cost, neighbor))
        
#negative indexing (-1) accesses elements from the end of the list. Therefore, path[-1] retrieves the most recent state configuration explored and added to path.
        if path[-1] != current_state:  # Avoid duplicate states
            path.append(current_state)

            print_state(current_state)
            print("Current heuristic : ",current_cost)
            print()
        
        steps += 1

    if current_cost > 0:
        print("No solution found")
    # A heuristic cost greater than 0 indicates that the algorithm has not yet reached the goal state or a state that satisfies the goal condition.

initial_state = tuple(map(int, input("Enter initial state : ").split()))
# tuple() is applied to the list of integers to convert it into a tuple. In Python, tuples are immutable (cannot be changed), which can be advantageous in certain contexts where immutability is desired, such as ensuring that the initial puzzle state remains unchanged during the solving process.
# inu = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# random.shuffle(inu)
# initial_state = tuple(inu)

# goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)
goal_state = tuple(map(int, input("Enter goal state : ").split()))

solve_puzzle(initial_state, goal_state)


# Enter initial state : 1 2 3 7 8 4 6 0 5
# Enter goal state : 1 2 3 8 0 4 7 6 5