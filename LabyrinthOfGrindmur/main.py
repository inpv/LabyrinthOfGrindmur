from tcod_init import Tcod


def main():
    Tcod.create_window(Tcod())


if __name__ == "__main__":
    """
    made to be able to include other modules from third-party software, like e.g. Pygame
    """
    main()
