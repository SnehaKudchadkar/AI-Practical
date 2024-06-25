def astar(graph, heuristic, start, goal):
    
    open_nodes = [(0, start)]   #open_nodes is a list of tuples, where each tuple contains the priority (f-value) and the node. Initially, it contains only the starting node with a priority of 0 (since the cost from the start to the start is zero)
    
    g_values = {node: float('inf') for node in graph}  #A dictionary comprehension is used to set the initial cost to reach every node to infinity (float('inf')), representing that they are initially unreachable.
   
    g_values[start] = 0    #Set the cost to reach the starting node to 0
    
    parents = {}        #This dictionary tracks the best path found to each node. It will be used to reconstruct the path once the goal is reached by storing the parent (previous node) for each node.

    while open_nodes:       #Continue the search as long as there are nodes to explore.

        open_nodes.sort()  # Sort the open_nodes based on the first element (priority). This ensures that the node with the smallest f-value is at the beginning of the list.

        current_priority, current_node = open_nodes.pop(0)   #The first element of the sorted open_nodes list (the node with the lowest priority) is removed and assigned to current_priority and current_node.

        if current_node == goal:

            path = []  #Initialize the list to store the path from the start node to the goal. This list will store the nodes in the path by backtracking from the goal to the start using the parents dictionary.
            
            #This loop appends the current node to the path list and updates current_node to its parent (from the parents dictionary) until current_node is None.
            while current_node:
                path.append(current_node)
                current_node = parents.get(current_node)
            
            return path[::-1], g_values[goal]  # Return the reconstructed path and the total cost to reach the goal. The path list is reversed to get the correct order from start to goal. The total cost to reach the goal is retrieved from g_values[goal].

        for neighbor in graph.get(current_node, {}):   #Retrieve the neighbors of current_node from the graph dictionary. If current_node has no neighbors, return an empty dictionary to avoid errors.
            
            tentative_g = g_values[current_node] + graph[current_node][neighbor]
                # g_values[current_node]: The cost to reach the current node from the start node.
                # graph[current_node][neighbor]: The cost to travel from the current node to its neighbor.
                # tentative_g: The sum of these two values, representing the cost to reach the neighbor node from the start node via the current node.    
            
            if tentative_g < g_values[neighbor]:  #Determine if the new path to the neighbor node is better (i.e., has a lower cost) than any previously found path.

                g_values[neighbor] = tentative_g   
                parents[neighbor] = current_node   # Record the current node as the parent of the neighbor node.
               
                f_value = tentative_g + heuristic[neighbor]
                    # tentative_g: The cost to reach the neighbor node from the start node.
                    # heuristic[neighbor]: The heuristic estimate of the cost from the neighbor node to the goal node.
                    # f_value: The sum of these two values, representing the total estimated cost to reach the goal.

                open_nodes.append((f_value, neighbor))
                # Add the neighbor node to the list of nodes to be explored.
                # open_nodes is a list of nodes to be explored, sorted by their f_value to ensure that nodes with the lowest estimated total cost are explored first.

    return None, float('inf')
    # Return a result indicating that no path was found.
    # This line is outside the loop and is executed if the loop completes without finding a path to the goal node.
    # None indicates that no path was found.
    # float('inf') represents the cost, indicating that it's infinitely large since no path exists.


graph = {}
heuristic = {}   #  This line initializes an empty dictionary called heuristic which will store the heuristic values for each node.
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):          #This is a for loop that iterates num_nodes times. The underscore _ is used as a loop variable. It's a common convention when the variable is not actually used in the loop body.
    node = input("Enter node: ")
    heuristic_value = float(input(f"Enter heuristic value for node {node}: "))   #float(input(...)) converts the input into a floating-point number and stores it in heuristic_value
    neighbors = input(f"Enter neighbors and costs for node {node}: ").split()   #Prompts the user to enter the neighbors and the associated costs for the current node. The input is a string where each neighbor and its cost are separated by spaces. For example, B,1 C,4.  .split() converts this string into a list of strings, splitting on spaces. For example, 'B,1 C,4' becomes ['B,1', 'C,4'] 
    graph[node] = {neighbor_cost.split(',')[0]: float(neighbor_cost.split(',')[1]) for neighbor_cost in neighbors}  # neighbor_cost.split(',')[0] extracts the neighbor's name. float(neighbor_cost.split(',')[1]) extracts the cost to reach that neighbor and converts it to a float.
    heuristic[node] = heuristic_value


start = input("Enter the starting node: ")
goal = input('Enter the goal node: ')

print() # creates a blank line

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Shortest path found:")
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found from the starting node to the goal node.")


# INPUT
# Enter the number of nodes: 4
# Enter node: A
# Enter heuristic value for node A: 7
# Enter neighbors and costs for node A: B,1 C,4
# Enter node: B
# Enter heuristic value for node B: 6
# Enter neighbors and costs for node B: C,2 D,5
# Enter node: C
# Enter heuristic value for node C: 2
# Enter neighbors and costs for node C: D,1
# Enter node: D
# Enter heuristic value for node D: 0
# Enter neighbors and costs for node D: 
# Enter the starting node: A
# Enter the goal node: D

# OUTPUT
# Shortest path found:
# Path: ['A', 'B', 'C', 'D']
# Cost: 4.0
