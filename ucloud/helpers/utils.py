# -*- coding: utf-8 -*-

import random
import base64

_lowercase = "abcdefghijklmnopqrstuvwxyz"
_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_numbers = "0123456789"
_specials = "_"


def gen_password(
    n,
    lower_letters=_lowercase,
    upper_letters=_uppercase,
    number_letters=_numbers,
    special_letters=_specials,
    min_lower=1,
    min_upper=1,
    min_number=1,
    min_specials=1,
):
    """ generate password for any resource

    >>> len(gen_password(20))
    20

    :param int n: password total length
    :param str lower_letters: all lowercase letters
    :param str upper_letters: all uppercase letters
    :param str number_letters: all number letters
    :param str special_letters: all special letters
    :param int min_lower: minimal number of lowercase letters
    :param int min_upper: minimal number of uppercase letters
    :param int min_number: minimal number of number letters
    :param int min_specials: minimal number of special letters
    :return:
    """
    all_letters = lower_letters + upper_letters + number_letters + special_letters
    minimal_total = min_lower + min_upper + min_number + min_specials
    if n < minimal_total:
        raise ValueError(
            "the length of password must be larger than total minimal letters number"
        )

    minimal_letters = sum([
        [random.choice(lower_letters) for i in range(min_lower)],
        [random.choice(upper_letters) for i in range(min_upper)],
        [random.choice(number_letters) for i in range(min_number)],
        [random.choice(special_letters) for i in range(min_specials)]
    ])

    additional_letters = random.sample(all_letters, n - minimal_total)
    results = minimal_letters + additional_letters
    random.shuffle(results)
    return "".join(results)


def first(l):
    if len(l) == 0:
        return None
    return l[0]


def b64encode(s):
    """

    >>> b64encode("foobar42")
    'Zm9vYmFyNDI='

    :param str s: input string
    :return: base64 string
    """
    return base64.b64encode(s.encode()).decode()


def b64decode(s):
    """

    >>> b64decode("Zm9vYmFyNDI=")
    'foobar42'

    :param str s: base64 string
    :return: output string
    """
    return base64.b64decode(s.encode()).decode()
