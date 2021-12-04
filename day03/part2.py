from __future__ import annotations

import argparse
import os.path
from collections import defaultdict

import pytest


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def count_occurrences(input_list) -> dict:
    kvmap = defaultdict(int)
    for k in input_list:
        kvmap[k] += 1
    return kvmap


def compute(s: str) -> int:
    lines = s.splitlines()
    ox_values_to_consider = lines
    co_values_to_consider = lines

    for i in range(len(lines[0])):
        # occurences.append(count_occurrences(values_to_consider))
        if len(ox_values_to_consider) > 1:
            ox_current_bit_occurrences = count_occurrences(
                [line[i] for line in ox_values_to_consider]
            )
            if ox_current_bit_occurrences["0"] == ox_current_bit_occurrences["1"]:
                ox_values_to_consider = [
                    line for line in ox_values_to_consider if line[i] == "1"
                ]
            elif ox_current_bit_occurrences["0"] > ox_current_bit_occurrences["1"]:
                ox_values_to_consider = [
                    line for line in ox_values_to_consider if line[i] == "0"
                ]
            else:
                ox_values_to_consider = [
                    line for line in ox_values_to_consider if line[i] == "1"
                ]

        if len(co_values_to_consider) > 1:
            co_current_bit_occurrences = count_occurrences(
                [line[i] for line in co_values_to_consider]
            )
            if co_current_bit_occurrences["0"] == co_current_bit_occurrences["1"]:
                co_values_to_consider = [
                    line for line in co_values_to_consider if line[i] == "0"
                ]
            elif co_current_bit_occurrences["0"] > co_current_bit_occurrences["1"]:
                co_values_to_consider = [
                    line for line in co_values_to_consider if line[i] == "1"
                ]
            else:
                co_values_to_consider = [
                    line for line in co_values_to_consider if line[i] == "0"
                ]

            # print(f"co_values_to_consider: {co_values_to_consider}")

    oxygen_value = int(ox_values_to_consider[0], 2)
    co2_value = int(co_values_to_consider[0], 2)

    print(f"Oxygen value: {oxygen_value}")
    print(f"CO2 value: {co2_value}")

    return oxygen_value * co2_value


INPUT_S = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 230),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
