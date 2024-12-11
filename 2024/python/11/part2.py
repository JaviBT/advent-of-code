from collections import defaultdict

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

stones = [int(x) for x in raw[0].split()]

def process_stones(stones, blinks):
    def split_stone(number):
        number_str = str(number)
        mid = len(number_str) // 2
        left = int(number_str[:mid]) if mid > 0 else 0
        right = int(number_str[mid:]) if mid < len(number_str) else 0
        return left, right

    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in range(blinks):
        new_counts = defaultdict(int)

        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_counts[stone * 2024] += count

        stone_counts = new_counts

    total_stones = sum(stone_counts.values())
    return total_stones

blinks = 75
final_stones = process_stones(stones, blinks)

print(final_stones)
