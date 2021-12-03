import argparse
from collections import Counter, deque


def get_bit_counts(lines):
    """Get counts of bit values in every position"""
    counters = [Counter() for _ in lines[0]]
    for line in lines:
        for counter, bit in zip(counters, line):
            counter[bit] += 1
    return counters


def calc_gamma_and_epsilon(bit_counts):
    """Return number made of most common bits"""
    gamma = int("".join((counter.most_common()[0][0] for counter in bit_counts)), 2)
    epsilon = int("".join((counter.most_common()[1][0] for counter in bit_counts)), 2)
    return gamma, epsilon


# TODO: Refactor these into single functions and don't bother
#       recalculating bit counts for positions we don't care about
def get_oxygen_rating(lines):
    """Filter lines according to some criteria until one number remains"""
    filtered_lines = deque(lines)
    for i in range(len(lines[0])):
        bit_counts = get_bit_counts(filtered_lines)
        pos_counts = bit_counts[i].most_common()
        if len(pos_counts) == 1:
            target_bit = pos_counts[0][0]
        else:
            target_bit = (
                "1" if pos_counts[0][1] == pos_counts[1][1] else pos_counts[0][0]
            )
        last_line = filtered_lines[-1]
        # print(filtered_lines)
        while len(filtered_lines) > 1:
            line = filtered_lines.popleft()
            if line[i] == target_bit:
                filtered_lines.append(line)
            if line == last_line:
                break
        if len(filtered_lines) == 1:
            # print(filtered_lines)
            break

    return int("".join(filtered_lines[0]), 2)


def get_co2_rating(lines):
    """Filter lines according to some criteria until one number remains"""
    filtered_lines = deque(lines)
    for i in range(len(lines[0])):
        bit_counts = get_bit_counts(filtered_lines)
        pos_counts = bit_counts[i].most_common()
        if len(pos_counts) == 1:
            target_bit = pos_counts[0][0]
        else:
            target_bit = (
                "0" if pos_counts[0][1] == pos_counts[1][1] else pos_counts[1][0]
            )
        last_line = filtered_lines[-1]
        # print(filtered_lines)
        while len(filtered_lines) > 1:
            line = filtered_lines.popleft()
            if line[i] == target_bit:
                filtered_lines.append(line)
            if line == last_line:
                break
        if len(filtered_lines) == 1:
            # print(filtered_lines)
            break

    return int("".join(filtered_lines[0]), 2)


def main():
    parser = argparse.ArgumentParser(
        description="Print gamma rate and epsilon rate of list of numbers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "input_file", help="File with numbers",
    )
    args = parser.parse_args()
    with open(args.input_file) as f:
        lines = [line.strip() for line in f]
    print(f"Number of lines in file: {len(lines)}")
    bit_counts = get_bit_counts(lines)
    # print(f"Bit counts: {bit_counts}")
    gamma, epsilon = calc_gamma_and_epsilon(bit_counts)
    print(f"Gamma: {gamma} Epsilon: {epsilon} Product: {gamma * epsilon}")
    oxygen_rating = get_oxygen_rating(lines)
    co2_rating = get_co2_rating(lines)
    print(
        f"Oxygen: {oxygen_rating} CO2: {co2_rating} Product: {oxygen_rating * co2_rating}"
    )


if __name__ == "__main__":
    main()
