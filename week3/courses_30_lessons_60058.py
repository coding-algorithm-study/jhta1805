from collections import deque, Counter


def is_right(st):
    stack = ['']
    for s in st:
        if stack[-1] + s == '()':
            stack.pop()
            continue
        stack.append(s)

    stack = [x for x in stack if x]
    if stack:
        return False

    return True


def solution(p):
    answer = ''
    lis = [x for x in p]

    def cutting(li):
        u = ''
        dq = deque(li)
        while len(li):
            u += dq.popleft()
            cnt = Counter(u)
            values = list(cnt.values())
            if len(cnt.keys()) % 2 == 0:
                if values[0] == values[1]:
                    return u, ''.join(dq)

    # )()(
    def validate(flag, s):
        nonlocal answer
        u, v = cutting(s)

        if flag and is_right(u):
            answer += u
            if v:
                validate(v)

        else:
            if v:
                validate(v)
            if not is_right(u):
                u = u[::-1]
                u = u[1:-1]
            else:
                u = ''

            v = '(' + v + ')' + u
            if is_right(v):
                answer = v
                return v

            validate(v)

    validate(lis)
    print(answer)
    return answer


if __name__ == '__main__':
    # assert solution(")(") == "()"
    # assert solution(")()(") == "(())"
    # assert solution("))))((((") == "()((()))"
    # assert solution("()") == "()"
    assert solution("(()())()") == "(()())()"
    # assert solution("()))((()") == "()(())()"
    # assert solution("(()())()()") == "(()())()()"
    # assert solution("(()())))()") == "(()())()()"
