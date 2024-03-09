from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_DataType = np.dtype(
    [
        ("character", np.int32),  # Unicode codepoint.
        ("foreground", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("background", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_DataType = np.dtype(
    [
        ("walkable", np.bool_),  # True if this tile can be walked over.
        ("transparent", np.bool_),  # True if this tile doesn't block FOV.
        ("dark", graphic_DataType),  # Graphics for when this tile is not in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_DataType)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (0, 0, 0)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (255, 255, 255), (0, 0, 100)),
)