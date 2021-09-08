import tcod.event
from typing import Optional
from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_w:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_s:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_a:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_d:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action

    def ev_windowresized(
        self, event: "tcod.event.WindowResized"
    ) -> Optional[Action]:
        pass  # The next call to context.new_console may return a different size.
