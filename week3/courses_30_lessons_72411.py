import array
from collections import Counter, defaultdict
from itertools import combinations


def solution(orders, course):
    # orders = sorted(orders)
    orders_ = sorted([k for k, v in Counter(s for x in orders for s in x).items() if v >= 2])
    match = defaultdict(dict)
    for idx in course:
        max_match = defaultdict(list)
        is_max = 0
        for combi in (x for x in combinations(orders_, idx)):
            # print(combi)
            match_li = []

            for order in orders:
                cnt = 0
                for c in combi:
                    if order.count(c):
                        cnt += 1

                if cnt == idx:
                    match_li.append(combi)
            count_match = len(match_li)
            if is_max <= count_match:
                is_max = count_match

            else:
                continue
            if count_match >= 2:
                max_match[count_match].append(''.join(combi))
        max_match = sorted(max_match.items(), reverse=True)
        # print(max_match)
        if max_match:
            match[idx] = max_match[0][1]
    answer = []
    for x in match.values():
        answer.extend(x)
    print(sorted(answer))
    return sorted(answer)


if __name__ == '__main__':
    # solution(['ABCDEFGHJ','BF','CF','DF'], [2, 3, 4])
    # assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) == ["AC", "ACDE", "BCFG", "CDE"]
    # assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]
    assert solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"]
    # assert solution(["AB", "AC", "AD", "ACD", "ADE", "ADEF", "ADEFG", "AEF"], [3, 5]) == ["ADE"]
