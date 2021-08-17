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
            answer += f'{int(x)}'
        except ValueError:
            s_ += x
            try:
                v = string_to_number[s_]
                answer += f'{v}'
                s_ = ''
            except KeyError:
                continue

    return int(answer)


if __name__ == '__main__':
    # assert solution("one4seveneight") == 1478
    assert solution("threeonezero") == 310
