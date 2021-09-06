from collections import defaultdict

HANDS = ('L', 'R')


def get_dist(direction, current):
    result = 0
    for d, c in zip(direction, current):
        result += abs(c - d)

    print('dist', result)
    return result


def solution(numbers, hand):
    hand = hand[0].upper()
    answer = ''
    matrix = defaultdict(list)

    key_pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    for row in range(0, 4):
        for column in range(0, 3):
            matrix[key_pad[row][column]] = [column, row]

    print(matrix)
    current_loc = ['*', '#']

    def vector(current):
        nonlocal current_loc
        if current % 3 == 1:
            current_loc[0] = current
            return 'L'

        if current % 3 == 0 and current != 0:
            current_loc[1] = current
            return 'R'

        if current % 3 == 2 or current == 0:
            left_dist = get_dist(matrix[current_loc[0]], matrix[current])
            right_dist = get_dist(matrix[current_loc[1]], matrix[current])
            if left_dist < right_dist:
                current_loc[0] = current
                return 'L'
            if left_dist > right_dist:
                current_loc[1] = current
                return 'R'
            if left_dist == right_dist:
                current_loc[HANDS.index(hand)] = current
                return hand
    for num in numbers:
        answer += vector(num)

    return answer


if __name__ == '__main__':
    # assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"
