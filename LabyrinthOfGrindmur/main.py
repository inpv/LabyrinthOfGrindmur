import tcod
import config
import tcod.event
import copy
import entity_factories
from input_handlers import EventHandler
from engine import Engine
from procgen import RectangularRoom

FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED


def main() -> None:

    # setting the necessary variables and class instances
    screen_width = 1920
    screen_height = 1200

    map_width = 72
    map_height = 38

    tileset = tcod.tileset.load_tilesheet(
        "rexpaint_cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    player = copy.deepcopy(entity_factories.player)

    event_handler = EventHandler()

    left_room = RectangularRoom.generate_room(int(map_width / 2), map_height, 0, 15, 14, 14, player)
    right_room = RectangularRoom.generate_room(int(map_width / 2), map_height, 20, 15, 14, 14, player)

    engine_left = Engine(event_handler=event_handler, game_map=left_room, player=player)
    engine_right = Engine(event_handler=event_handler, game_map=right_room, player=player)

    # creating the window
    with tcod.context.new(  # New window with pixel resolution of width × height.

        width=screen_width,
        height=screen_height,
        sdl_window_flags=FLAGS,
        tileset=tileset,
        title="Labyrinth Of Grindmur",
        vsync=False

    ) as context:

        while True:
            # creating the consoles
            console_main = tcod.Console(width=map_width, height=map_height, order="F")

            left_width = int(console_main.width / 2)
            right_width = console_main.width - left_width

            console_left = tcod.Console(width=left_width, height=console_main.height, order="F")
            console_right = tcod.Console(width=right_width, height=console_main.height, order="F")

            engine_left.render(console=console_left)
            engine_right.render_light(console=console_right)

            console_left.blit(console_main, dest_x=0, dest_y=0, width=left_width, height=screen_height)
            console_right.blit(console_main, dest_x=right_width, dest_y=0, width=right_width, height=screen_height)

            context.present(console_main, keep_aspect=False, integer_scaling=True)
            console_main.clear()

            # handling the events
            events = tcod.event.wait()
            engine_left.handle_events(events)
            engine_right.handle_events(events)


if __name__ == "__main__":
    main()
