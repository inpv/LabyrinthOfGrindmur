import random
import tile_types


class MazeGen:

    cell = tile_types.floor
    wall = tile_types.wall
    maze = []

    def __init__(self, width, height):

        self.width = width // 2 * 2 + 1
        self.height = height // 2 * 2 + 1

        # this creates a 2d-array for your maze data (False: path, True: wall)
        # 0 - Path, 1 - Wall, 2 - Border
        self.grid = [
                      [1 for x in range(self.width)]
                      for y in range(self.height)
                     ]

        self.create_maze(x=0, y=0)

    def set_path(self, x, y):
        self.grid[y][x] = 0

    def set_wall(self, x, y):
        self.grid[y][x] = 1

    # a function to return if the current cell is a wall,
    #  and if the cell is within the maze bounds
    def is_wall(self, x, y):
        # checks if the coordinates are within the maze grid
        if 0 <= x < self.width and 0 <= y < self.height:
            # if they are, then we can check if the cell is a wall
            return self.grid[y][x]
        # if the coordinates are not within the maze bounds, we don't want to go there
        else:
            return 0

    def create_maze(self, x, y):
        # set the current cell to a path, so that we don't return here later
        self.set_path(x, y)
        # we create a list of directions (in a random order) we can try
        all_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        random.shuffle(all_directions)

        # we keep trying the next direction in the list, until we have no directions left
        while len(all_directions) > 0:

            # we remove and return the last item in our directions list
            direction_to_try = all_directions.pop()

            # calculate the new node's coordinates using our random direction.
            # we *2 as we are moving two cells in each direction to the next node
            node_x = x + (direction_to_try[0] * 2)
            node_y = y + (direction_to_try[1] * 2)

            # check if the test node is a wall (eg it hasn't been visited)
            if self.is_wall(node_x, node_y):
                # success code: we have found a path

                # set our linking cell (between the two nodes we're moving from/to) to a path
                link_cell_x = x + direction_to_try[0]
                link_cell_y = y + direction_to_try[1]
                self.set_path(link_cell_x, link_cell_y)

                # "move" to our new node. remember we are calling the function every
                #  time we move, so we call it again but with the updated x and y coordinates
                self.create_maze(node_x, node_y)

        return  # back to the function to backtrack

    def main(self):
        # transforms the maze into tile-based format

        MazeGen.maze = [[1 for y in range(self.height)] for x in range(self.width)]

        conv = {
            1: MazeGen.wall,
            0: MazeGen.cell,
        }

        for y in range(0, self.height):
            for x in range(0, self.width):
                """
                # Create border walls dynamically
                if self.grid[0][x] == 0 or self.grid[0][x] == 1:  # if either wall or path, create border wall
                    self.grid[0][x] = 2

                if self.grid[y][0] == 0 or self.grid[y][0] == 1:
                    self.grid[y][0] = 2

                if self.grid[self.height-1][x] == 0 or self.grid[self.height-1][x] == 1:
                    self.grid[self.height-1][x] = 2

                if self.grid[y][self.width-1] == 0 or self.grid[y][self.width-1] == 1:
                    self.grid[y][self.width-1] = 2
                """

                MazeGen.maze[y][x] = (conv[self.grid[y][x]])

        return MazeGen.maze
