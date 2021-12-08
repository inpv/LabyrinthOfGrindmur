from __future__ import annotations
import config
from typing import Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    from game_map import GameMap


class Action:

    def __init__(self, entity: Entity) -> None:
        super().__init__()
        self.entity = entity

    @property
    def game_map(self) -> GameMap:
        game_map = None
        # """Return the engine this action belongs to."""

        if self.entity == config.player:
            game_map = config.left_room
        elif self.entity == config.npc:
            game_map = config.right_room

        return game_map

    def perform(self) -> None:
        """
        Perform this action with the objects needed to determine its scope.
        `self.engine` is the scope this action is being performed in.
        `self.entity` is the object performing the action.
        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self) -> None:
        raise SystemExit()


class ActionWithDirection(Action):
    def __init__(self, entity: Entity, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Returns this actions destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this actions destination.."""
        return self.game_map.get_blocking_entity_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()


class MovementAction(ActionWithDirection):

    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.

        if not self.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile.

        if self.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return  # Destination is blocked by an entity.

        self.entity.move(self.dx, self.dy)


class ResizeAction(Action):

    def perform(self):
        pass
