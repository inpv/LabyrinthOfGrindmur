import tcod
import tcod.event
import color
import config
from engine import Engine
from procgen import Dungeon

FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED


class Tcod:

    def __init__(self):

        # setting the constants

        self.screen_width = 1920
        self.screen_height = 1200

        self.map_width = 72
        self.map_height = 38

        # loading tileset

        self.tileset = tcod.tileset.load_tilesheet(
            "rexpaint_cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437
        )

        # generating maps with entities

        config.left_room = Dungeon.generate_room(
            int(self.map_width / 2),
            self.map_height, 0, 15, 14, 14)

        config.right_room = Dungeon.generate_room(
            int(self.map_width / 2),
            self.map_height, 20, 15, 14, 14)

        # initializing engine

        self.engine = Engine(entities=[config.player, config.npc],
                             game_maps=[config.left_room, config.right_room])

        self.engine.update_fov()

        # displaying messages

        self.engine.message_log.add_message(
            "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
        )

    def create_window(self):
        # creating the window
        with tcod.context.new(  # New window with pixel resolution of width × height.

            width=self.screen_width,
            height=self.screen_height,
            sdl_window_flags=FLAGS,
            tileset=self.tileset,
            title="Labyrinth Of Grindmur",
            vsync=False

        ) as context:

            while True:
                # creating the consoles
                console_main = tcod.Console(width=self.map_width, height=self.map_height, order="F")

                left_width = int(console_main.width / 2)
                right_width = console_main.width - left_width

                console_left = tcod.Console(width=left_width, height=console_main.height, order="F")
                console_right = tcod.Console(width=right_width, height=console_main.height, order="F")

                self.engine.render(console=console_left)
                self.engine.render_light(console=console_right)

                console_left.blit(console_main, dest_x=0, dest_y=0, width=left_width, height=self.screen_height)
                console_right.blit(console_main, dest_x=right_width, dest_y=0, width=right_width, height=self.screen_height)

                context.present(console_main, keep_aspect=False, integer_scaling=True)
                console_main.clear()

                # handling the events
                self.engine.event_handler.handle_events()
