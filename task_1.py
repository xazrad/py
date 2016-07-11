# _*_ coding: utf-8 _*_


''' Решения
1.  parse_string_re - с помощью регулярных выражений.
    Решение: "Вычленить" неверную конечную часть строки (*** или ((*** и т. д.

2.  parse_string -  решение без помощи регулярных выражений.
    Решение: Решение схоже с предыдущим.
    Обратным перебором "вычленяю" неверную конечную часть.
'''

import argparse
import re


parser = argparse.ArgumentParser(description='Run option')
parser.add_argument('value', help='string value')


def parse_string_re(value):
    pattern = r'[(]+[.^(]*[^)]*$'
    p = re.compile(pattern, re.I | re.U | re.DOTALL)
    match = p.search(value)
    if match is None:
        return value
    return value[:match.start()]


def parse_string(value):
    stop = None

    for ind, s in enumerate(value[::-1]):
        if s == '(':
            stop = ind+1
            continue
        if s == ')':
            stop = ind
            break

    if stop:
        return value[:-stop]
    return value


if __name__ == '__main__':
    pars_args = parser.parse_args()
    value = pars_args.value
    print 'Input data: %s' % value

    result_re = parse_string_re(value)
    result = parse_string(value)

    print 'Result with regex: %s' % result_re
    print 'Result without regex: %s' % result
