from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Any
from tcod.console import Console
from tcod.map import compute_fov

import config
from entity import Entity
from message_log import MessageLog
from procgen import RectangularRoom
from input_handlers import EventHandler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap


class Engine:
    # game_map: GameMap

    def __init__(self, player: Entity):
        self.event_handler: EventHandler = EventHandler(self)

        self.player = player

        if player == config.player:
            self.game_map = config.left_room
        elif player == config.npc:
            self.game_map = config.right_room

        self.message_log = MessageLog()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities:
            if entity == config.player:
                pass
            elif entity == config.npc:
                print(f'The {entity.name} wonders when it will get to take a real turn.')

    def update_fov(self) -> None:
        # Recompute the visible area based on the players point of view.
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=1,
        )

        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:

        self.game_map.render(console)

        self.message_log.render(console=console, x=0, y=0, width=30, height=5)

    def render_light(self, console: Console) -> None:

        self.game_map.render_light(console)
