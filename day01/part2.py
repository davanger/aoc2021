from __future__ import annotations

import argparse
import os.path

import pytest

# from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    for n in numbers:
        pass

    # lines = s.splitlines()
    depths = [int(line) for line in s.splitlines()]

    previous_depth = None
    increases = 0

    max_window_idx = len(depths) - 2

    for i in range(max_window_idx):
        measurement = sum(depths[i: (i + 3)])
        if previous_depth is not None and (measurement > previous_depth):
            increases += 1
        previous_depth = measurement

    return increases


INPUT_S = os.path.join(os.path.dirname(__file__), "input_sample.txt")


@pytest.mark.parametrize(
    ("input_s", "expected"), ((INPUT_S, 5),),
)
def test(input_s: str, expected: int) -> None:
    with open(input_s) as f:
        assert compute(f.read()) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
