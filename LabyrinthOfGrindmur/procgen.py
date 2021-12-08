import config
import random
from typing import Tuple
from game_map import GameMap
from mazegen import MazeGen
from entity import Entity
import entity_factories
import config
import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class RectangularRoom:

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
    def generate_maze(room_width, room_height):  # for each maze
        maze_width = room_width - 1
        maze_height = room_height - 1
        config.maze_raw = MazeGen.main(MazeGen(maze_width, maze_height))

        return config.maze_raw

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
    def generate_room(
        map_width,
        map_height,
        x,
        y,
        room_width,
        room_height,
    ) -> GameMap:  # for each room

        entity = None

        # decide which entry to load unto the map based on the maps' coordinates

        if x == 0:
            config.player = copy.deepcopy(entity_factories.player)
            entity = config.player
        elif x == 20:
            config.npc = copy.deepcopy(entity_factories.npc)
            entity = config.npc

        game_map = GameMap(map_width, map_height, entities=[entity])

        maze = RectangularRoom.generate_maze(14, 14)
        room = RectangularRoom(x, y, room_width, room_height)

        game_map.tiles[room.inner] = maze

        RectangularRoom.place_entities(room, game_map)

        return game_map

