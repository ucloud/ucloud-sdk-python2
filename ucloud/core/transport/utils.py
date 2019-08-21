# -*- coding: utf-8 -*-

import codecs

_null = "\x00".encode("ascii")
_null2 = _null * 2
_null3 = _null * 3


def guess_json_utf(data):
    """ guess_json_utf will detect the encoding of bytes,
    see `requests.utils.guess_json_utf`

    :rtype: str
    """
    sample = data[:4]
    if sample in (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE):
        return "utf-32"
    if sample[:3] == codecs.BOM_UTF8:
        return "utf-8-sig"
    if sample[:2] in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
        return "utf-16"
    nullcount = sample.count(_null)
    if nullcount == 0:
        return "utf-8"
    if nullcount == 2:
        if sample[::2] == _null2:
            return "utf-16-be"
        if sample[1::2] == _null2:
            return "utf-16-le"
    if nullcount == 3:
        if sample[:3] == _null3:
            return "utf-32-be"
        if sample[1:] == _null3:
            return "utf-32-le"
    return None
