def main(x: list) -> int:
    str_0 = str(x[0]) + str(x[1]) + str(x[4]) + str(x[2])
    str_2 = str(x[0]) + str(x[1]) + str(x[4]) + str(x[3])
    str_4 = str(x[0]) + str(x[1])
    str_7 = str(x[0]) + str(x[4]) + str(x[1])
    str_9 = str(x[0]) + str(x[4])
    if str_0 == 'C++19792001SAGE':
        return 0
    if str_0 == 'C++19792001PLSQL':
        return 1
    if str_2 == 'C++197919831982':
        return 2
    if str_2 == 'C++197919831962':
        return 3
    if str_4 == 'C++1981':
        return 4
    if str_4 == 'EQ1979':
        return 5
    if str_4 == 'EQ1981':
        return 6
    if str_7 == 'R20011979':
        return 7
    if str_7 == 'R20011981':
        return 8
    # if str_9 == 'R1983':
    return 9
    # tmp
    # if tmp_1 and x[2] == 'SAGE':
    #     return 0
    # if tmp_1 and x[2] == 'PLSQL':
    #     return 1
    # if tmp_1 and x[4] == 1983 and x[3] == 1982:
    #     return 2
    # if tmp_1 and x[4] == 1983 and x[3] == 1962:
    #     return 3
    # if x[0] == 'C++' and x[1] == 1981:
    #     return 4
    # if x[0] == 'EQ' and x[1] == 1979:
    #     return 5
    # if x[0] == 'EQ' and x[1] == 1981:
    #     return 6
    # if x[0] == 'R' and x[4] == 2001 and x[1] == 1979:
    #     return 7
    # if x[0] == 'R' and x[4] == 2001 and x[1] == 1981:
    #     return 8
    # if x[0] == 'R' and x[4] == 1983:
    #     return 9
    # if x[0] == 'C++':
    #     if x[1] == 1979:
    #         if x[4] == 2001:
    #             if x[2] == 'SAGE':
    #                 return 0
    #             elif x[2] == 'PLSQL':
    #                 return 1
    #         elif x[4] == 1983:
    #             if x[3] == 1982:
    #                 return 2
    #             elif x[3] == 1962:
    #                 return 3
    #     elif x[1] == 1981:
    #         return 4
    # elif x[0] == 'EQ':
    #     if x[1] == 1979:
    #         return 5
    #     elif x[1] == 1981:
    #         return 6
    # elif x[0] == 'R':
    #     if x[4] == 2001:
    #         if x[1] == 1979:
    #             return 7
    #         elif x[1] == 1981:
    #             return 8
    #     elif x[4] == 1983:
    #         return 9
    # print(main(['EQ', 1979, 'SAGE', 1962, 1983]))
    # print(main(['R', 1981, 'PLSQL', 1982, 2001]))
    # print(main(['R', 1979, 'SAGE', 1962, 1983]))
    # print(main(['C++', 1979, 'PLSQL', 1962, 2001]))
    # print(main(['C++', 1981, 'SAGE', 1982, 1983]))
