import tcod
import tcod.event
from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import RectangularRoom

FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED


def main() -> None:

    # setting the necessary variables and class instances
    screen_width = 1920
    screen_height = 1200

    map_width = 64
    map_height = 37

    tileset = tcod.tileset.load_tilesheet(
        "rexpaint_cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    player = Entity(21, 16, "@", (255, 255, 255))
    npc = Entity(36, 16, "S", (255, 255, 0))

    entities = {npc, player}

    event_handler = EventHandler()
    game_map = RectangularRoom.generate_dungeon(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # creating the window
    with tcod.context.new(  # New window with pixel resolution of width × height.

        width=screen_width,
        height=screen_height,
        sdl_window_flags=FLAGS,
        tileset=tileset,
        title="Labyrinth Of Grindmur",
        vsync=True

    ) as context:

        while True:
            # creating the console
            console = context.new_console(min_columns=10, min_rows=10, magnification=3.0, order="F")
            # console = tcod.Console(*context.recommended_console_size(), order="F")
            engine.render(console=console, context=context)

            # handling the events
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
