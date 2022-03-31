import tile_types


class MazeGen:

    cell = tile_types.floor
    wall = tile_types.wall
    exit_door = tile_types.exit_door
    entrance_door = tile_types.entrance_door

    conv = {
        0: cell,
        1: wall,
        2: entrance_door,
        3: exit_door
    }

    @staticmethod
    def main(grid_arr):
        # transforms the maze into tile-based format

        maze_height = len(grid_arr)
        maze_width = len(grid_arr[0])
        maze = [[1 for y in range(maze_height)] for x in range(maze_width)]

        for y in range(0, maze_height):
            for x in range(0, maze_width):
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

                if grid_arr[maze_height - 1][maze_width - 1] == 0:
                    grid_arr[maze_height - 1][maze_width - 1] = 3

                if grid_arr[0][0] == 0:
                    grid_arr[0][0] = 2
                """

                maze[y][x] = (MazeGen.conv[grid_arr[y][x]])

        return maze
