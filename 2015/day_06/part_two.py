import re
from pathlib import Path

from rich import print
from rich.traceback import install


def read_input_file() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        return stream.readlines()


def solution(input_data: list[str]) -> int:
    lights = {(x, y): 0 for x in range(1000) for y in range(1000)}
    regex = r"(.*) (\d+,\d+).*?(\d+,\d+)"
    for command in input_data:
        match = re.search(regex, command)
        if not match:
            continue
        state = match.group(1)
        start = tuple(int(x) for x in match.group(2).split(","))
        end = tuple(int(x) for x in match.group(3).split(","))
        temp = start
        while temp[0] <= end[0]:
            while temp[1] <= end[1]:
                if state == "turn on":
                    lights[temp] += 1
                elif state == "turn off":
                    if lights[temp] != 0:
                        lights[temp] -= 1
                elif state == "toggle":
                    lights[temp] += 2

                temp = (temp[0], temp[1] + 1)
            temp = (temp[0] + 1, start[1])
    return sum(lights.values())


def main() -> None:
    if not (input_data := read_input_file()):
        return

    brightness = solution(input_data=input_data)
    print(f"Part Two: {brightness}")


# region testing
def examples() -> None:
    brightness = solution(input_data=["turn on 0,0 through 0,0"])
    assert brightness == 1
    brightness = solution(input_data=["toggle 0,0 through 999,999"])
    assert brightness == 2000000


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
