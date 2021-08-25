def solution(s):
    string_to_number = dict(
        zero=0,
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
    )
    answer = ''
    s_ = ''
    for x in s:
        try:
            answer += f'{int(x)}' # o
        except ValueError:
            s_ += x
            try:
                v = string_to_number[s_]
                answer += f'{v}'
                s_ = ''
            except KeyError:
                continue

    return int(answer)


def solution2(s):
    string_to_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = s
    for idx, string in enumerate(string_to_numbers):
        answer = answer.replace(string, str(idx))

    return int(answer)


def other_solution2(s):
    string_to_number = dict(
        zero=0,
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
    )
    answer = s
    for k, v in string_to_number.items():
        answer = answer.replace(k, str(v))

    return int(answer)


if __name__ == '__main__':
    assert solution("one4seveneight") == 1478
    assert solution("threeonezero") == 310

    assert solution2("one4seveneight") == 1478
    assert solution2("threeonezero") == 310

    assert other_solution2("one4seveneight") == 1478
    assert other_solution2("threeonezero") == 310
