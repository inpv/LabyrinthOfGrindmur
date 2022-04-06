import config
import random
from typing import Tuple
from game_map import GameMap
from gridgen import GridGen
from mazegen import MazeGen
from mazesolve import MazeSolver
from entity import Entity
import entity_factories
import config
import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Dungeon:

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

    @staticmethod
    def generate_maze(room_width, room_height):  # for each maze
        maze_width = room_width - 1
        maze_height = room_height - 1

        grid = GridGen.get_grid(GridGen(maze_width, maze_height))
        config.maze_raw = grid

        return MazeGen.main(grid)

    @staticmethod
    def place_entities(room, dungeon: GameMap) -> None:
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        # entity_factories.npc.spawn(dungeon, 21, 16)  # test!!!

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):

            # entity_factories.npc.spawn(dungeon, x, y)

            if random.random() < 0.8:
                pass  # Place a buff there
            else:
                pass  # Place a debuff there

    @staticmethod
    def generate_room(  # generates each room turnkey, with all the bells and whistles
        map_width,
        map_height,
        room_x_coord,
        room_y_coord,
        room_width,
        room_height,
    ) -> GameMap:

        # we don't know which entity should load during class initialization
        entity = None

        # decide which entity to load unto the game map based on the maps' coordinates

        if room_x_coord == 0:
            config.player = copy.deepcopy(entity_factories.player)
            entity = config.player
        elif room_x_coord == 20:
            config.npc = copy.deepcopy(entity_factories.npc)
            entity = config.npc

        # generate the raw game map object
        game_map = GameMap(map_width, map_height, entities=[entity])

        # generate the mazes to different variables
        config.maze_left = Dungeon.generate_maze(14, 14)
        maze = config.maze_left
        config.maze_counter += 1

        if config.maze_counter > 1:
            # config.maze_right_raw = GridGen.main(self=GridGen(14, 14))
            config.maze_right = Dungeon.generate_maze(14, 14)
            maze = config.maze_right

            config.maze_path = MazeSolver.solve_maze(config.maze_raw)

        room = Dungeon(room_x_coord, room_y_coord, room_width, room_height)

        # fill the room with tiles
        game_map.tiles[room.inner] = maze

        # place all the entities
        Dungeon.place_entities(room, game_map)

        return game_map
