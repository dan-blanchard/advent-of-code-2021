import argparse
from collections import Counter, deque, defaultdict


def parse_input_file(input_file):
    lines = input_file.readlines()
    print(f"Number of lines in file: {len(lines)}")
    drawn_numbers = [int(num) for num in lines[0].split(',')]
    grids = [[[int(num) for num in line.split()] for line in lines[i: i + 5]] for i in range(2, len(lines), 6)]
    return drawn_numbers, grids


def determine_winner(drawn_numbers, grids):
    nums_to_positions = defaultdict(list)
    for i, grid in enumerate(grids):
        for j, row in enumerate(grid):
            for k, num in enumerate(row):
                nums_to_positions[num].append((i, j, k))

    score = winner = None
    for drawn in drawn_numbers:
        if drawn in nums_to_positions:
            for (i, j, k) in nums_to_positions[drawn]:
                grids[i][j][k] = 'X'
            for grid_num, grid in enumerate(grids):
                for row in grid:
                    if row.count('X') == 5:
                        winner = grid_num
                        break
                for i in range(5):
                    if all(row[i] == 'X' for row in grid):
                        winner = grid_num
                        break
                if winner:
                    break
        if winner:
            score = sum(sum(x for x in row if x != 'X') for row in grids[winner] * drawn)
            break

    return winner, score





def main():
    parser = argparse.ArgumentParser(
        description="Parse bingo file and determine winner",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input_file", help="File with numbers",
    )
    args = parser.parse_args()
    with open(args.input_file) as f:
        drawn_numbers, grids = parse_input_file(f)
    print(f"Drawn numbers: {drawn_numbers}")
    print(f"Grids: {grids}")
    winner, score = determine_winner(drawn_numbers, grids)
    print(f"Winner: {winner}")
    print(f"Winner: {score}")


if __name__ == "__main__":
    main()
