#M and C BFS

# append is used with lists. []
# add is used with sets. {}

# append preserves the order of elements in the list. The new element is added to the end.
# add does not guarantee any order because sets are unordered collections.

# append allows duplicates because lists can contain repeated elements.
# add does not allow duplicates because sets are collections of unique elements.


from collections import deque


def is_valid(state):

    m1, c1, n = state  # Unpack the current state into the number of missionaries (m1), cannibals (c1), and boat position (n)
    m2 = m - m1        # Calculate the number of missionaries on the other side (right bank)
    c2 = c - c1        # Calculate the number of cannibals on the other side (right bank)

    # Check for negative values, which are invalid
    if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False

    # Ensure the missionaries are not outnumbered by cannibals on either side, if there are missionaries present
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False

    # If all checks pass, the state is valid
    return True

def generate_successors(state):

    m, c, n = state  # Unpack the current state into the number of missionaries (m), cannibals (c), and boat position (n)
    #The state is a tuple (m, c, n).
    #m is the number of missionaries on the left bank.
    #c is the number of cannibals on the left bank.
    #n indicates the boat's position (1 if on the left bank, 0 if on the right bank).
    
    successors = []  # Initialize an empty list to hold valid successor states

    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Define all possible actions (combinations of missionaries and cannibals that can move)

    for action in actions:
        moved_ms, moved_cn = action  # Unpack the action into the number of missionaries and cannibals to move

        if n == 1:  # If the boat is on the left bank
            new_state = (m - moved_ms, c - moved_cn, 0)  # Move the boat to the right bank
        else:  # If the boat is on the right bank
            new_state = (m + moved_ms, c + moved_cn, 1)  # Move the boat to the left bank
            
        if is_valid(new_state):  # Check if the new state is valid
            successors.append(new_state)  # If valid, add the new state to the list of successors

    return successors  # Return the list of valid successor states


def bfs():
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)

    visited = set()
    queue = deque([(start_state,[])])

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        
        path.append(state)
        
        if state == goal_state:
            allpaths.append(path)
            continue

        visited.add(state)

        for successor in generate_successors(state):
            if successor not in visited:
                queue.append((successor,path.copy()))

                # successor is the new state to be explored.
                # path.copy() creates a copy of the current path list and appends the successor state to it. This ensures that each path is uniquely tracked and extended independently of others.
                # The .copy() method is used to avoid modifying the original path list, as lists are mutable in Python.


allpaths = []

m = int(input("No. of Missionaires : "))
c = int(input("No. of Cannibals : "))
b = int(input("Boat size: "))

bfs()

if len(allpaths)==0:
    print("No Solutions")
else:
     for p in allpaths:
        print(p)


# INPUT
# M = 3
# C = 3
# Boat size = 2