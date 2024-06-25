# Baisc BFS

from collections import deque

print('Breadth First Search (BFS)')

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

# The range function provides a sequence of numbers that are used as indices to access elements in the matrix. It ensures that the loops iterate the correct number of times to cover all rows and columns of the matrix.

for i in range(rows):
    
    row = []
    
    for j in range(cols):

        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)

    matrix.append(row)


def bfs(matrix, start):

    num_vertices = len(matrix)

    visited = [False] * num_vertices 
    # [False] * num_vertices creates a list with num_vertices elements, all set to False.
    # Each element in the visited list corresponds to a vertex in the graph. The index of the list represents the vertex number, and the value (False) indicates that the vertex has not been visited yet.
  
    queue = deque([start])

    visited[start] = True
    # starting vertex is correctly initialized as visited.
   
    while queue:

        current_node = queue.popleft()
    
        if current_node==0:
            print(f"{current_node}",end="")

# indicates the starting vertex or the first vertex visited.
# If current_node is 0, it prints just the vertex number (0) without the arrow ->, ensuring the path starts with the vertex number alone.
    
        else:
            print(f" -> {current_node}",end="")

        for neighbor in range(num_vertices):
            if matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# matrix[current_node][neighbor] == 1: This condition checks if there is an edge (connection) between current_node and neighbor. In adjacency matrix representation:
# 1 typically denotes an edge exists between the vertices.
# 0 denotes no edge.
# not visited[neighbor]: Ensures that neighbor has not been visited before. This prevents revisiting vertices and ensures each vertex is processed only once.

print("\nStarting BFS from node 0")
bfs(matrix, 0)

