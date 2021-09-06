def solution(s: str):
    result = []
    for idx in range(0, len(s) // 2 + 1):
        idx = idx or 1
        parsing = s[0:idx]
        nxt = s[idx+1:]

if __name__ == '__main__':
    # assert solution("aabbaccc") == 7
    # assert solution("ababcdcdababcdcd") == 9
    assert solution("a") == 1
    # assert solution("abcabcdede") == 8
    # assert solution("abcabcabcabcdededededede") == 14
    # assert solution("xababcdcdababcdcd") == 17