from collections import namedtuple

ACTION_MAPPER = {
    'Enter': '들어왔습니다.',
    'Leave': '나갔습니다.',
}


def announce(action, nickname):
    return f'{nickname}님이 {ACTION_MAPPER[action]}'


def solution(record):
    answer = []
    di = {}
    # user = namedtuple('User', ['idx', 'action', 'uid', 'nickname'], defaults=('',))
    # s = sorted(((idx, *x.split()) for idx, x in enumerate(record)), key=lambda x: (x[1], -x[0]))
    for x in record:
        x = x.split()
        if x[0] == 'Leave':
            continue
        di[x[1]] = x[2]

    for x in record:
        x = x.split()
        if x[0] == 'Change':
            continue
        answer.append(announce(x[0], di[x[1]]))

    return answer


if __name__ == '__main__':
    assert solution([
        "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"
    ]) == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

    assert solution([
        "Enter uid1234 Muzi", "Change uid1234 Ryan"
    ]) == ["Ryan님이 들어왔습니다."]

    assert solution([
        "Enter uid1234 Muzi", "Enter uid1235 Ryan", "Leave uid1234",  "Enter uid4567 Prodo"
    ]) == ["Muzi님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Muzi님이 나갔습니다.", "Prodo님이 들어왔습니다."]
