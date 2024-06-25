#Water Jug DFS

# append is used with lists. []
# add is used with sets. {}

# append preserves the order of elements in the list. The new element is added to the end.
# add does not guarantee any order because sets are unordered collections.

# append allows duplicates because lists can contain repeated elements.
# add does not allow duplicates because sets are collections of unique elements.


from collections import deque

def WaterJugDFS(goal,Left_Capacity,Right_Capacity):

    visited = set()
    stack = deque([(0, 0, [(0, 0)])])  #current state and path

    while stack:
        Left, Right, path = stack.pop()

        if Left == goal or Right == goal:
            allpath.append(path)
            continue

        visited.add((Left,Right))

        succ = [(Left_Capacity, Right), (Left, Right_Capacity), (0, Right), (Left, 0)]

        SpaceLeft = Left_Capacity - Left
        if SpaceLeft >= Right:
            succ.append((Left + Right, 0))
        else:
            succ.append((Left_Capacity, Right - SpaceLeft))
            
        SpaceRight = Right_Capacity - Right
        if SpaceRight >= Left:
            succ.append((0, Left + Right))
        else:
            succ.append((Left - SpaceRight, Right_Capacity))

        for s in succ:
            if s not in visited:
                stack.append((s[0], s[1],path + [s] )) #left jug , right jug , path


allpath = []

print("Water Jug Problem (DFS)")

goal = int(input("Enter Goal "))
Left_Capacity = int(input("Enter Capacity of Left Jug : "))
Right_Capacity = int(input("Enter Capacity of Right Jug : "))
WaterJugDFS(goal,Left_Capacity,Right_Capacity)

if len(allpath)==0:
    print("No Solutions")
else:
     for p in allpath:
        print(p)

# INPUT
# Goal: 2
# LEFT: 4
# RIGHT: 3