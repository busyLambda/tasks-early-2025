import enum
from typing import Dict, List

DEBUG: bool = False

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

DICE_SET: List[Dice] = [
    Dice.D20,
    Dice.D10,
    Dice.D8,
    Dice.D6,
    Dice.D4,
    Dice.D3,
    Dice.D2
]

def range_to_dice_notation(min_val: int, max_val: int) -> str:
    output_dice_set: Dict[Dice, int] = {}

    r: int = max_val - min_val

    # A clone of r meant for statekeeping mutation in order to get the amount of dice we need for the input range.
    r_mut_clone: int = r
    total_dice_count: int = 0
    for dice in DICE_SET:
        dice_count: int = r_mut_clone // (dice.value-1)
        if dice_count != 0:
            r_mut_clone -= dice_count * dice.value
            output_dice_set[dice] = dice_count
            total_dice_count += dice_count
            r_mut_clone += dice_count
            # Break early to not loop the rest of the die in uselessly since no die will match 1 or 0.
            if r_mut_clone <= 1:
                break

    offset: int = 0
    if total_dice_count > min_val:
        offset = -(total_dice_count+(r-max_val))
    elif total_dice_count < min_val:
        offset = total_dice_count

    # d = (d)ice
    # c = dice_(c)ount
    output = ""
    for i in range(len(DICE_SET)-1, -1, -1):
        dice = DICE_SET[i]
        if dice not in output_dice_set:
            continue
        count = output_dice_set[dice]
        if count != 0:
            output+=f"{count}d{dice.value}"
            if i != 0:
                output+="+"

    output+=str(offset)

    return output

for l in input.split("\n")[:-1]:
    y = l.split(" ")
    min_val = int(y[0])
    max_val = int(y[1])

    print(range_to_dice_notation(min_val, max_val))
