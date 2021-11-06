from typing import Tuple
from game_map import GameMap
from mazegen import MazeGen


class RectangularRoom:

    maze = None

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    # SAME ENGINE RENDERS DIFFERENT ROOMS DIFFERENTLY
    # two rooms with different params
    # engine chooses, which room to render, based on them

    @staticmethod
    def generate_room(x, y, room_width, room_height):
        room = RectangularRoom(x=x, y=y, width=room_width, height=room_height)

        return room

    @staticmethod
    def generate_maze(room_width, room_height):
        maze_width = room_width - 1
        maze_height = room_height - 1
        RectangularRoom.maze = MazeGen.main(MazeGen(maze_width, maze_height))

        return RectangularRoom.maze

    @staticmethod
    def generate_map(map_width, map_height, x, y, room_width, room_height) -> GameMap:
        game_map = GameMap(map_width, map_height)
        game_map.tiles[RectangularRoom.generate_room(x, y, room_width, room_height).inner] = \
            RectangularRoom.generate_maze(room_width, room_height)

        return game_map
