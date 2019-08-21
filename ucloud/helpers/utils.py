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
    all_letters = "".join(
        [lower_letters, upper_letters, number_letters, special_letters]
    )
    minimal_total = min_lower + min_upper + min_number + min_specials
    if n < minimal_total:
        raise ValueError(
            "the length of password must be larger than total minimal letters number"
        )
    minimal_letters = "".join(
        [
            gen_string(lower_letters, min_lower),
            gen_string(upper_letters, min_upper),
            gen_string(number_letters, min_number),
            gen_string(special_letters, min_specials),
        ]
    )
    additional_letters = random.sample(all_letters, n - minimal_total)
    results = list(minimal_letters) + additional_letters
    random.shuffle(results)
    return "".join(results)


def gen_string(letters, length):
    return "".join([random.choice(letters) for i in range(length)])


def first(l):
    if len(l) == 0:
        return None
    return l[0]


def b64encode(s):
    """ base64 encode

    :param str s: input string
    :return: base64 string
    """
    return base64.b64encode(s.encode()).decode()


def b64decode(s):
    """ base64 decode

    :param str s: base64 string
    :return: output string
    """
    return base64.b64decode(s.encode()).decode()
