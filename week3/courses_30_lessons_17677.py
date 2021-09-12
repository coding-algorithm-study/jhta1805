import math
import re
from collections import Counter


def cutting_len(s):
    l = len(s)
    if l % 2:
        return (l // 2) + 1
    else:
        return l // 2


regex = re.compile('[a-z]')


def check_str(string):
    li = []
    for idx in range(len(string)):
        s = string[idx:idx + 2]
        # if len(s) == 1:
        #     s = string[idx - 1:idx]
        m = regex.findall(s)
        if len(m) != 2:
            continue

        li.append(s)
    return li


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    li1 = check_str(str1)
    li2 = check_str(str2)
    cnt1 = Counter(li1)
    cnt2 = Counter(li2)
    intersection = 0
    union = 0
    for k, v in cnt1.items():
        if cnt2.get(k):
            num2 = cnt2.pop(k)
            intersection += min(v, num2)
            union += max(v, num2)
            continue

        union += v

    union += sum(x for x in cnt2.values())
    if not intersection and not union:
        intersection, union = [1, 1]
    return math.trunc((intersection / union ) * 65536)


if __name__ == '__main__':
    # assert solution('FRANCE', 'french') == 16384
    # assert solution('handshake', 'shake hands') == 65536
    assert solution('aa', 'shake hands') == 0
    # assert solution('aa1+aa2', 'AAAA12') == 43690
    # assert solution('E=M*C^2', 'e=m*c^2') == 65536

    # solution('FRANCE', 'french')
    # solution('handshake', '	shake hands')
    # solution('aa1+aa2', 'AAAA12')
    # solution('E=M*C^2', 'e=m*c^2')
