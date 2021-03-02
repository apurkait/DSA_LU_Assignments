if __name__ == '__main__':
    t = int(input())
    res = ''
    b = 0
    flag_decimal = False  # setting a flag just to avoid redundant checking
    for st in input().split():
        count_one = st.count('1')
        count_zero = st.count('0')
        if not flag_decimal and len(st) - count_zero - count_one > 0:
            flag_decimal = True
            res += st
        else:
            b += count_zero

    if res == '':
        res = '1' + '0' * b
    else:
        res += '0' * b
    print(res)
