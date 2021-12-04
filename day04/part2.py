import argparse
import os.path
from typing import List

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


class BingoCard:
    def __init__(self, number_rows: list, id: int):
        self.id = id
        self.number_rows = [self.parse_line(line) for line in number_rows]
        self.marked_numbers = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

    def check_row(self, row_index: int) -> bool:
        return all(self.marked_numbers[row_index])

    def check_column(self, column_index: int) -> bool:
        column_elements = [row[column_index] for row in self.marked_numbers]
        return all(column_elements)

    def parse_line(self, line: str) -> list:
        return [int(x) for x in line.split()]

    def mark_number(self, number: int):
        for row in range(5):
            for column in range(5):
                if self.number_rows[row][column] == number:
                    self.marked_numbers[row][column] = 1

    def check_victory(self) -> bool:
        return any([self.check_row(i) for i in range(5)]) or any(
            [self.check_column(i) for i in range(5)]
        )

    def calculate_score(self, current_number: int) -> int:
        total_sum = 0
        for row in range(5):
            for column in range(5):
                if not self.marked_numbers[row][column]:
                    total_sum += self.number_rows[row][column]

        return total_sum * current_number


def compute(s: str) -> int:
    all_lines = s.splitlines()
    bingo_cards = []

    balls = [int(number) for number in all_lines[0].split(",")]

    card_lines = all_lines[2:]

    while "" in card_lines:
        card_lines.remove("")

    total_cards = len(card_lines) // 5
    already_won = []

    for i in range(total_cards):
        initial_line = 5 * i
        current_card_lines = card_lines[initial_line : initial_line + 5]
        bingo_cards.append(BingoCard(current_card_lines, i))

    for ball in balls:
        for card in bingo_cards:
            if card.id in already_won:
                continue
            card.mark_number(ball)

        for card in bingo_cards:
            if card.id in already_won:
                continue
            if card.check_victory():
                already_won.append(card.id)
                if len(already_won) == total_cards:
                    return card.calculate_score(ball)

    return 0


INPUT_S = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, 1924),),
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
