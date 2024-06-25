#M and C DFS

# append is used with lists. []
# add is used with sets. {}

# append preserves the order of elements in the list. The new element is added to the end.
# add does not guarantee any order because sets are unordered collections.

# append allows duplicates because lists can contain repeated elements.
# add does not allow duplicates because sets are collections of unique elements.

from collections import deque

def is_valid(state):

    m1, c1, n = state
    m2 = m - m1
    c2 = c - c1

    if m1 < 0  or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    
    if  (m1 and m1 < c1)  or (m2 and m2 < c2):
        return False
    
    return True

def generate_successors(state):
    m, c, n = state
    successors = []

    actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for action in actions:
        moved_ms, moved_cn =action

        if n == 1:
            new_state = (m - moved_ms, c - moved_cn, 0)
        else:
            new_state = (m + moved_ms, c + moved_cn, 1)
            
        if is_valid(new_state):
            successors.append(new_state)

    return successors

def dfs():
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)

    visited = set()
    stack = deque([(start_state,[])])

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue
        
        path.append(state)
        
        if state == goal_state:
            allpaths.append(path)
            continue

        visited.add(state)

        for successor in generate_successors(state):
            if successor not in visited:
                stack.append((successor,path.copy()))

allpaths = []

m = int(input("No. of Missionaires : "))
c = int(input("No. of Cannibals : "))
b = int(input("Boat size: "))

dfs()

if len(allpaths)==0:
    print("No Solutions")
else:
     for p in allpaths:
        print(p)


# INPUT
# M = 3
# C = 3
# Boat size = 2