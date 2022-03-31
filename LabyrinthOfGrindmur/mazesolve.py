class Node:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.direction_number = 0


class MazeSolver:

    maze_solve_stack = []

    # End coordinates (fx and fy): (len(maze) - 1), (len(maze[0]) - 1)

    @staticmethod
    def is_reachable(maze_arr, fx, fy):

        # maze of rows*columns matrix

        rows = len(maze_arr)
        columns = len(maze_arr[0])

        # Initially setting the visited
        # array to false (unvisited)
        visited = [[False] * rows for _ in range(columns)]

        # Initially starting at (0, 0).
        i = 0
        j = 0

        MazeSolver.maze_solve_stack = []

        temp = Node(i, j)

        MazeSolver.maze_solve_stack.append(temp)

        while MazeSolver.maze_solve_stack:

            # Pop the top node and move to the
            # left, right, top, down or retract
            # back according the value of node's
            # dirn variable.
            temp = MazeSolver.maze_solve_stack.pop()
            d = temp.direction_number
            i = temp.x
            j = temp.y

            # Increment the direction and
            # push the node in the stack again.
            temp.direction_number += 1
            MazeSolver.maze_solve_stack.append(temp)

            # If we reach the Food coordinates
            # return true
            if i == fx and j == fy:
                return True

            # Checking the Up direction.
            if d == 0:
                if i - 1 >= 0 and (maze_arr[i - 1][j] == 0 or maze_arr[i - 1][j] == 3) and not visited[i - 1][j]:
                    temp1 = Node(i - 1, j)
                    visited[i - 1][j] = True
                    MazeSolver.maze_solve_stack.append(temp1)

            # Checking the left direction
            elif d == 1:
                if j - 1 >= 0 and (maze_arr[i][j - 1] == 0 or maze_arr[i][j - 1] == 3) and not visited[i][j - 1]:
                    temp1 = Node(i, j - 1)
                    visited[i][j - 1] = True
                    MazeSolver.maze_solve_stack.append(temp1)

            # Checking the down direction
            elif d == 2:
                if i + 1 < rows and (maze_arr[i + 1][j] == 0 or maze_arr[i + 1][j] == 3) and not visited[i + 1][j]:
                    temp1 = Node(i + 1, j)
                    visited[i + 1][j] = True
                    MazeSolver.maze_solve_stack.append(temp1)

            # Checking the right direction
            elif d == 3:
                if j + 1 < columns and (maze_arr[i][j + 1] == 0 or maze_arr[i][j + 1] == 3) and not visited[i][j + 1]:
                    temp1 = Node(i, j + 1)
                    visited[i][j + 1] = True
                    MazeSolver.maze_solve_stack.append(temp1)

            # If none of the direction can take
            # the rat to the Food, retract back
            # to the path where the rat came from.
            else:
                visited[temp.x][temp.y] = False
                MazeSolver.maze_solve_stack.pop()

        # If the stack is empty and
        # no path is found return false.
        return False

    @staticmethod
    def solve_maze(maze_arr):
        if MazeSolver.is_reachable(maze_arr, len(maze_arr) - 1, len(maze_arr[0]) - 1):
            return MazeSolver.maze_solve_stack
        else:
            pass
