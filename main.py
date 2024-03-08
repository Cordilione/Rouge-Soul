#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from inputHandlers import EventHandler

def main() -> None:
    screen_width = 100
    screen_height = 70

    playerX = int(screen_width / 2)
    playerY = int(screen_height / 2)


    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Rouge Soul Dev Test",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=playerX, y=playerY, string="@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    playerX += action.xDirection
                    playerY += action.yDirection

                elif isinstance(action, EscapeAction):
                    raise SystemExit()



if __name__ == "__main__":
    main()