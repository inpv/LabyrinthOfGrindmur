"""
def main() -> None:

    screen_width = 80
    screen_height = 60

    tileset = tcod.tileset.load_tilesheet(
        "rexpaint_cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    root_console = tcod.Console(screen_width, screen_height, order="F")

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Labyrinth Of Grindmur",
            vsync=True,
    ) as context:

        while True:
            root_console.clear()
            root_console.print(x=0, y=0, string="@")
            context.present(root_console)

            for event in tcod.event.wait():
                context.convert_event(event)
                print(event)
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()
"""