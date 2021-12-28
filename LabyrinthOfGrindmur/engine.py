from __future__ import annotations
from typing import TYPE_CHECKING, Iterable, Any, List
from tcod.console import Console
from tcod.map import compute_fov

import config
from message_log import MessageLog
from input_handlers import EventHandler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap


class Engine:

    def __init__(self, entities: List[Entity], game_maps: List[GameMap]):
        self.event_handler: EventHandler = EventHandler(self)

        self.entities = entities
        self.game_maps = game_maps

        self.message_log = MessageLog()

    def handle_enemy_turns(self) -> None:
        for game_map in self.game_maps:
            for entity in game_map.entities:
                if entity == config.player:
                    pass
                elif entity == config.npc:
                    print(f'The {entity.name} wonders when it will get to take a real turn.')

    def update_fov(self) -> None:
        # Recompute the visible area based on the players point of view.
        for game_map in self.game_maps:
            for entity in game_map.entities:
                if entity == config.player:
                    game_map.visible[:] = compute_fov(
                        game_map.tiles["transparent"],
                        (entity.x, entity.y),
                        radius=1,
                    )

                    # If a tile is "visible" it should be added to "explored".
                    game_map.explored |= game_map.visible

                elif entity == config.npc:
                    pass

    def render(self, console: Console) -> None:

        for game_map in self.game_maps:
            if game_map == config.left_room:
                game_map.render(console)
                self.message_log.render(console=console, x=0, y=0, width=30, height=5)

    def render_light(self, console: Console) -> None:

        for game_map in self.game_maps:
            if game_map == config.right_room:
                game_map.render_light(console)
