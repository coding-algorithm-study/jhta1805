from collections import Counter


def solution(N, stages):
    counts = Counter(stages)
    answer = {}
    participants = len(stages)
    for i in range(1, N + 1):
        fail = counts.get(i) or 0
        answer[i] = fail / (participants or 1)
        participants -= fail

    return sorted(answer.keys(), key=lambda x: (-answer[x], x))


if __name__ == '__main__':
    # assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
    # assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
    # assert solution(4, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]) == [4, 2, 3, 1]
    assert solution(5, [2, 1, 2, 4, 2, 4, 3, 3]) == [4, 3, 2, 1, 5]
