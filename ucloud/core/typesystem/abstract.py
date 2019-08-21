# -*- coding: utf-8 -*-

from ucloud.core import exc


class Field(object):
    def __init__(
        self,
        required=False,
        default=None,
        dump_to=None,
        load_from=None,
        strict=None,
        **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs
        self.strict = bool(strict)

    def dumps(self, value, **kwargs):
        raise NotImplementedError

    def loads(self, value, **kwargs):
        raise NotImplementedError

    @staticmethod
    def fail(name, expected, got):
        msg = "invalid field {}, expect {}, got {}".format(name, expected, got)
        raise exc.ValidationException(msg)


class Schema(object):
    fields = {}

    def __init__(
        self,
        required=False,
        default=dict,
        dump_to=None,
        load_from=None,
        strict=False,
        case_sensitive=False,
        **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs
        self.strict = strict
        self.case_sensitive = case_sensitive

    def dumps(self, d):
        raise NotImplementedError

    def loads(self, d):
        raise NotImplementedError
