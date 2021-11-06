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

    map_width = 72
    map_height = 38

    tileset = tcod.tileset.load_tilesheet(
        "rexpaint_cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    player = Entity(1, 16, "@", (255, 255, 255))
    npc = Entity(21, 16, "S", (255, 255, 0))

    entities = {npc, player}

    event_handler = EventHandler()

    RectangularRoom.maze = RectangularRoom.generate_maze(14, 14)
    left_room = RectangularRoom.generate_map(int(map_width / 2), map_height, 0, 15, 14, 14)
    right_room = RectangularRoom.generate_map(int(map_width / 2), map_height, 20, 15, 14, 14)

    engine_left = Engine(entities=entities, event_handler=event_handler, game_map=left_room, player=player, npc=npc)
    engine_right = Engine(entities=entities, event_handler=event_handler, game_map=right_room, player=player, npc=npc)

    # main engine renders entities and their actions, the two others render the rooms
    # main engine and room engine

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

            """
            if console.width == left_width:
                engine_left.render(console=console)
            else if console.width == right_width:
                engine_right.render_light(console=console)
            """

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
