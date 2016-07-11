# _*_ coding: utf-8 _*_

import pytest

from task_1 import parse_string, parse_string_re


# tuple() - first - value; second - expected result
TEST_DATA = [
    ('esdfd((esdf)(esdf', 'esdfd((esdf)'),  # from example
    ('abc', 'abc'),
    ('abc((', 'abc'),
    ('a(bc((', 'a'),
    ('(a(bc((', ''),
    (')(a(bc((', ')'),
    ('abc((a)', 'abc((a)'),
    ('abc((3)((', 'abc((3)'),
    ('abc((3\t\r)((', 'abc((3\t\r)'),
    ('abc((3\t\r)((22\t', 'abc((3\t\r)'),
    (u'эюя', u'эюя'),
    (u'эюя((', u'эюя'),
    (u'эюя((()', u'эюя((()'),
    ('a+8**bc($3#(+@!#(', 'a+8**bc'),
]


@pytest.mark.parametrize("value,expected", TEST_DATA)
def test_parse_string_re(value, expected):
    result = parse_string_re(value)
    assert result == expected


@pytest.mark.parametrize("value,expected", TEST_DATA)
def test_parse_string(value, expected):
    result = parse_string(value)
    assert result == expected
