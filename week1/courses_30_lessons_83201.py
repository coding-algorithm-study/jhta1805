RANKS = (
    (90, 101, 'A'),
    (80, 90, 'B'),
    (70, 80, 'C'),
    (50, 70, 'D'),
    (0, 50, 'F'),
)

def rank(score):
    for r in RANKS:
        if r[0] <= score < r[1]:
            return r[2]

def solution(scores):
    self_scores = [scores[idx][idx] for idx, _ in enumerate(scores)]
    pivot_scores = list(map(list, zip(*scores)))
    scores = []
    for idx, x in enumerate(pivot_scores):
        ss = self_scores[idx]
        if ss in [max(x), min(x)] and x.count(ss) == 1:
            x.remove(ss)

        scores.append(x)

    answer = [rank(sum(x) / len(x)) for x in scores]

    return ''.join(answer)


if __name__ == '__main__':
    assert solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                     [24, 90, 94, 75, 65]]) == "FBABD"

    assert solution([[50, 90], [50, 87]]) == "DA"
