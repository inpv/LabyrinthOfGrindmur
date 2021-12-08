from entity import Entity
from game_map import GameMap
from typing import Iterable, Optional, TYPE_CHECKING

player = Entity(Optional[GameMap], 1, 16, char="@", color=(255, 255, 255), name="Player", blocks_movement=True)
npc = Entity(Optional[GameMap], 21, 16, char="S", color=(255, 255, 0), name="Enemy", blocks_movement=True)
