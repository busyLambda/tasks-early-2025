import enum
from typing import Dict

DEBUG: bool = False

def debug(msg: str):
    if DEBUG:
        print(f"DEBUG: {msg}")

with open('./input.txt', 'r') as f:
  input: str = f.read()

class Dice(enum.Enum):
    D20 = 20
    D10 = 10
    D8  = 8
    D6  = 6
    D4  = 4
    D3  = 3
    D2  = 2

def calculate_offset(min_val: int, max_val: int, total_dice_count: int, dice_sum: int) -> int:
    """Kiszámolja az offsetet a választott kockák mennyisége és sum-ja illetve a minimum és maximum érték alapján.

    Args:
        min_val (int): Az input range minimum értéke. (min_val < max_val)
        max_val (int): Az input range maximum értéke. (max_val > min_val)
        total_dice_count (int): Az eddig kiválasztott kockák mennyisége.
        dice_sum (int): Az eddig kiválasztott kockák értékeinek a sum-ja.

    Returns:
        int: Az adott bemenetnek megfelelő offset érték.
    """

    if total_dice_count > min_val:
        return min_val - total_dice_count
    elif total_dice_count < min_val:
        if (dice_sum + total_dice_count) == max_val:
            return total_dice_count
        else:
            return min_val - total_dice_count
    else:
        return min_val - total_dice_count

def range_to_dice_notation(min_val: int, max_val: int) -> str:
    """Átvált egy bemeneti range (minimum és maximum) értéket a dice-notation változatára a lehető legkevesebb kocka felhasználásával.

    Args:
        min_val (int): Az input range minimum értéke. (min_val < max_val)
        max_val (int): Az input range maximum értéke. (max_val > min_val)

    Returns:
        str: A bemenet dice-notation-ben kifejezve.
    """
    output_dice_set: Dict[Dice, int] = {}

    target: int = max_val - min_val

    total_dice_count: int = 0
    dice_sum: int = 0
    for dice in Dice:
        dice_count: int = target // (dice.value-1)
        if dice_count != 0:
            output_dice_set[dice] = dice_count

            target -= dice_count * dice.value

            total_dice_count += dice_count
            target += dice_count
            dice_sum += dice.value

    offset: int = calculate_offset(min_val, max_val, total_dice_count, dice_sum)

    dice_formatted: list[str] = []
    for dice in reversed(Dice):
        if dice not in output_dice_set:
            continue

        count = output_dice_set[dice]
        if count != 0:
            dice_formatted.append(f"{count}d{dice.value}")

    return "+".join(dice_formatted)+f"{offset:+}"

for l in input.split("\n")[:-1]:
    parts = l.split(" ")

    min_val = int(parts[0])
    max_val = int(parts[1])

    print(range_to_dice_notation(min_val, max_val))
