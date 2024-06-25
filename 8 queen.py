import random

def heuristic(board):
    conflicts = 0

#  for i in range(len(board)): This outer loop iterates over each row (i) of the chessboard.
# for j in range(i+1, len(board)): This inner loop iterates over subsequent rows (j) starting from i+1. This ensures that we only compare each pair of queens once, avoiding redundant checks (e.g., comparing row 1 with row 2 and then row 2 with row 1).
    for i in range(len(board)):
        for j in range(i+1, len(board)):

# if board[i] == board[j]: Checks if two queens are in the same column
# abs(i - j) == abs(board[i] - board[j]): Checks if two queens threaten each other diagonally.
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                
                conflicts += 1

    return conflicts

def solve_queens(initial_board):

    current_board = initial_board.copy()
    current_heuristic = heuristic(current_board)
    print("Initial Board:", current_board)
    print("Initial Heuristic:", current_heuristic)

    same_state_count = 0
    #keeps track of how many times in a row you've made a move without making the situation better.
    # If you make a move to rearrange queens but it doesn't reduce the number of times they threaten each other, you increase same_state_count.
    
    max_same_state_count = 3 
    # This variable sets a threshold for same_state_count after which the algorithm triggers a random restart or some other strategy to escape the local minimum. 
    # if same_state_count reaches 3 (i.e., the algorithm has made 3 consecutive non-improving moves):
    # The algorithm will perform a random move (swap two rows) to attempt a different configuration.
    # After triggering this random move, same_state_count is reset to 0 to start counting again.

    while current_heuristic > 0:
        
        row1, row2 = random.sample(range(1, 9), 2) # This line generates a list of 2 random numbers from the range 1 to 8 (inclusive). These numbers represent the rows (or queens) that will be swapped on the chessboard.Example: If row1 = 3 and row2 = 7, it means we'll swap the queens in rows 3 and 7.
        current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1] # Swapping Queens on the Board (current_board):

        new_heuristic = heuristic(current_board)

        if new_heuristic < current_heuristic:
            
            current_heuristic = new_heuristic
            same_state_count = 0  # Reset same state counter
            
            print("Current Board:", current_board)
            print("Current Heuristic:", current_heuristic)

        else:
            # Undo the move if it doesn't lead to improvement
            current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1]
            same_state_count += 1

        #to solve local minima
        if same_state_count >= max_same_state_count:
            # Perform a random move to a neighboring state
            row1, row2 = random.sample(range(1, 9), 2)
            current_board[row1-1], current_board[row2-1] = current_board[row2-1], current_board[row1-1]
            same_state_count = 0  # Reset same state counter

    print("Solution Found!")
    print("Final Board:", current_board)
    print("Final Heuristic:", current_heuristic)


initial_board = []
t=8

print("Initial Board")
while t:
    inp=int(input())  # column is input and row is the index
    initial_board.append(inp)
    t=t-1  

solve_queens(initial_board)


# INPUT

# The list [0, 1, 2, 3, 4, 5, 6, 7] means:

# Queen in row 0 is placed in column 0.
# Queen in row 1 is placed in column 1.
# Queen in row 2 is placed in column 2.
# Queen in row 3 is placed in column 3.
# Queen in row 4 is placed in column 4.
# Queen in row 5 is placed in column 5.
# Queen in row 6 is placed in column 6.
# Queen in row 7 is placed in column 7.

# Q . . . . . . .
# . Q . . . . . .
# . . Q . . . . .
# . . . Q . . . .
# . . . . Q . . .
# . . . . . Q . .
# . . . . . . Q .
# . . . . . . . Q
