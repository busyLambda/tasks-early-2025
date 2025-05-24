import ast
from typing import List, Tuple, Dict, Set
from collections import deque

DEBUG: bool = False

def debug(msg: str) -> None:
    if DEBUG:
        print(f"DEBUG: {msg}")

with open('./input.txt', 'r') as f:
    input = f.read()

def decode_signals(days_input: List[Tuple[List[str], List[str]]]) -> Dict[str, str]:
    days = []
    codes_to_days: Dict[str, List[int]] = {}
    for i, (codes, events) in enumerate(days_input):
        required_events = set(events)
        days.append({
            'codes': codes,
            'required_events': required_events
        })
        for code in codes:
            if code not in codes_to_days:
                codes_to_days[code] = []
            codes_to_days[code].append(i)

    code_possible: Dict[str, Set[str]] = {}
    for code in codes_to_days:
        possible = None
        for day_idx in codes_to_days[code]:
            day_req = days[day_idx]['required_events']
            if possible is None:
                possible = day_req.copy()
            else:
                possible.intersection_update(day_req)
        code_possible[code] = possible.copy() if possible is not None else set()

    queue = deque()
    assigned: Dict[str, str] = {}
    for code, possible in code_possible.items():
        if len(possible) == 1:
            queue.append(code)

    while queue:
        current_code = queue.popleft()
        if current_code in assigned:
            continue
        current_possible = code_possible[current_code]
        if len(current_possible) != 1:
            continue
        event = current_possible.pop()
        assigned[current_code] = event
        current_possible.add(event)

        for day_idx in codes_to_days.get(current_code, []):
            day = days[day_idx]
            if event in day['required_events']:
                day['required_events'].remove(event)
                for other_code in day['codes']:
                    if other_code == current_code or other_code in assigned:
                        continue
                    new_possible = None
                    for other_day_idx in codes_to_days[other_code]:
                        other_day_req = days[other_day_idx]['required_events']
                        if new_possible is None:
                            new_possible = other_day_req.copy()
                        else:
                            new_possible.intersection_update(other_day_req)
                        if not new_possible:
                            break
                    if new_possible is None:
                        new_possible = set()
                    if new_possible != code_possible[other_code]:
                        code_possible[other_code] = new_possible
                        if len(new_possible) == 1:
                            queue.append(other_code)

    return assigned

def main() -> None:
    decoded: Dict[str, str] = decode_signals(ast.literal_eval(input))

    output: str = ""

    decoded_items = decoded.items()
    decoded_items_length: int = len(decoded_items)
    i: int = 0
    for code, event in decoded_items:
        output += f"\t\"{code}\": \"{event}\""
        if i+1 != decoded_items_length:
            output += ",\n"
        else:
            output += "\n"

        i += 1


    print(f"{{\n{output}}}")

if __name__ == '__main__':
    main()
