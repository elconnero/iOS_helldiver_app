import random
from typing import List, Set
from backend.universal.enums import War_Bond, Penetration

def build_pick_order(players: int) -> List[int]:
    """
    Return a random order of player numbers 1..players.

    Example: players=4 -> [3, 1, 4, 2]
    """
    order = list(range(1, players + 1))  # [1, 2, ..., players]
    random.shuffle(order)                # shuffle in-place
    return order

def convert_warbond_strings_to_enums(raw_warbonds: List[str]) -> Set[War_Bond]:
    """
    Take ['BASE', 'STEELD_VETERANS'] and return
    {War_Bond.BASE, War_Bond.STEELD_VETERANS}.
    """
    result: Set[War_Bond] = set()
    for wb_str in raw_warbonds:
        try:
            enum_value = War_Bond[wb_str]   # "BASE" -> War_Bond.BASE
        except KeyError:
            raise ValueError(f"Unknown warbond: {wb_str}")
        result.add(enum_value)
    return result