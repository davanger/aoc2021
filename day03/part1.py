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
    occurences = []
    for i in range(len(lines[0])):
        values_to_consider = [line[i] for line in lines]
        occurences.append(count_occurrences(values_to_consider))

    gamma_rate = "".join(
        ["1" if (occurence["1"] > occurence["0"]) else "0" for occurence in occurences]
    )
    epsilon_rate = "".join(
        ["1" if (occurence["1"] < occurence["0"]) else "0" for occurence in occurences]
    )

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    return gamma_rate * epsilon_rate


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
    ((INPUT_S, 198),),
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
