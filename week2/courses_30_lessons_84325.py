def solution(table, languages, preference):
    di = dict(zip(languages, preference))
    table_di = {}
    for t in table:
        t = t.split(" ")
        table_di[t[0]] = sum([(5 - idx) * (di.get(ln) or 0) for idx, ln in enumerate(t[1:])])

    return sorted(table_di.items(), key=lambda x: (x[0], x[1]))[::-1][0][0]


if __name__ == '__main__':
    # assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
    #                  "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
    #                  "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]) == 'HARDWARE'

    assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                     "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]) == 'PORTAL'

    assert solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                     "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                     "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA"], [7]) == 'SI'
