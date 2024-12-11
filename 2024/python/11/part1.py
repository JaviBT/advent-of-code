raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

stones = [int(x) for x in raw[0].split()]

def process_stones(stones, blinks):
    def split_stone(number):
        number_str = str(number)
        mid = len(number_str) // 2
        left = int(number_str[:mid]) if mid > 0 else 0
        right = int(number_str[mid:]) if mid < len(number_str) else 0
        return [left, right]

    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.extend(split_stone(stone))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

blinks = 25
final_stones = process_stones(stones, blinks)

print(len(final_stones))
