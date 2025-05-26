DEBUG: bool = False

def debug(msg: str) -> None:
    if DEBUG:
        print(f"DEBUG: {msg}")

class Gear:
    def __init__(self) -> None:
        self.index = 2
        self.values = [1, 2, 3]

    def turn_forward(self) -> None:
        if self.index+1 == len(self.values):
            self.index=0
        else:
            self.index+=1

def pull_lever(lever: list[int], gears: list[Gear]) -> None:
    """Szimulálja egy kar meghúzását a gears paraméter mutálása által.

    Args:
        lever (list[int]): Egy kar három egész számból álló listaként. (x ∈ list && 0 <= x <= 1) (len(gears) == len(lever))
        gears (list[gear]): A fogaskerekek. (len(gears) == len(lever))

    Returns:
        None: A függvény a gears paramétert mutálja így nincs return érték.
    """
    if len(gears) != len(lever):
        debug("Lever-gear length mismatch (should be impossible because we get correct input)!")

    for i in range(len(lever)):
        if lever[i] == 1:
            gears[i].turn_forward()

LEFT_LEVER: list[int] = [1, 1, 0]
RIGHT_LEVER: list[int] = [0, 1, 1]

def get_rotations(target: list[int], max_rotations: int = 8) -> str:
    """Úgy forgatja a fogaskerekeket, hogy azok a target paraméter értékét adják ki.

    Args:
        target (list[int]): Az állapot amelyet szeretnénk elérni.
        max_rotations (int): A maximális forgatások száma amivel elérhetjük a target-et.

    Returns:
        str: A target eléréséhez szükséges kar húzások space-el elválasztva vagy a "Megoldhatatlan" érték.

    """

    gears: list[Gear] = [
        Gear(),
        Gear(),
        Gear(),
    ]

    left: int = target[0]
    center: int = target[1]
    right: int = target[2]

    side_rotations: int = left+right
    if side_rotations > max_rotations:
        return "Megoldhatatlan"
    for i in range(side_rotations):
        pull_lever(LEFT_LEVER, gears)
    if gears[1].values[gears[1].index] == center:
        return " ".join(
            ["left" for _ in range(left)] +
            ["right" for _ in range(right)]
        )
    else:
        return "Megoldhatatlan"

def main() -> None:
    input: str = ""
    with open('./input.txt', 'r') as f:
      input = f.read()

    for line in input.split("\n")[:-1]:
        debug(line)
        if len(line)>9:
            x: list[str] = line.split("] ")
            max_rotations: int = int(x[1])
            target: list[int] = [int(y) for y in x[0].replace("[", "").split(", ")]

            print(get_rotations(target, max_rotations))
        else:
            target: list[int] = [int(x) for x in line.strip("[]").split(", ")]
            print(get_rotations(target))

if __name__ == '__main__':
    debug(f"\n---\n{input}---")
    main()
