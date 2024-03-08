class Action:
    pass


class EscapeAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, xDirection: int, yDirection: int):
        super().__init__()

        self.xDirection = xDirection
        self.yDirection = yDirection