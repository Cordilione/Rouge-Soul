from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x  # Entity's X coordinate
        self.y = y  # Entity's Y coordinate
        self.char = char  # Entity's Character or Icon
        self.color = color  # Entity's character Color

    def move(self, xDirection: int, yDirection: int) -> None:
        # Move the entity by a given amount
        self.x += xDirection
        self.y += yDirection
