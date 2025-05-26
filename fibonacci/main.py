DEBUG: bool = False

def debug(msg: str) -> None:
    if DEBUG:
        print(f"DEBUG: {msg}")

def parse_input_line(line: str) -> int | None:
    """Átalakítja használható adattá az input egy sorát(pozitív egész szám).

    Args:
        line (str): Az input fájl egy sora.

    Returns:
        int: Siker esetén vissza adja a bemeneti soron lévő számot.
        None: Hiba esetén None-t ad vissza.
    """
    stripped_line = line.strip()
    if not stripped_line:
        return None
    try:
        n = int(stripped_line)
    except ValueError:
        return None
    if n < 0:
        return None
    return n

def generate_fibonacci_up_to(n: int) -> list[int]:
    fib_numbers = []
    a, b = 0, 1
    while a <= n:
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

def filter_divisible_by_three(numbers: list[int]) -> list[int]:
    return [x for x in numbers if x % 3 == 0]

def process_line(line: str) -> str:
    """Feldolgoz egy sort az input-ból és vissza adja a megoldást.

    Args:
        line (str): az input fájl egy sora. Egyetlen pozitív egész számot tartalmaz.

    Returns:
       str: A feladat megoldása az adott bemeneti sorhoz(N/A ha nincs megoldás az inputhoz).
    """
    NO_SOLUTION: str = "N/A"

    n = parse_input_line(line)
    if n is None:
        return NO_SOLUTION

    fib_numbers = generate_fibonacci_up_to(n)
    filtered = filter_divisible_by_three(fib_numbers)

    if not filtered:
        return NO_SOLUTION

    return ", ".join(map(str, filtered))

def main() -> None:
    with open('./input.txt', 'r') as f:
        input_lines = f.read().splitlines()
    for line in input_lines:
        result = process_line(line)
        print(result)

if __name__ == "__main__":
    main()
