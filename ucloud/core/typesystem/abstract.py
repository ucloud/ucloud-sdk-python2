# -*- coding: utf-8 -*-


class Field(object):
    def __init__(
        self, required=False, default=None, dump_to=None, load_from=None, **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs

    def dumps(self, value, **kwargs):
        raise NotImplementedError

    def loads(self, value, **kwargs):
        raise NotImplementedError


class Schema(object):
    fields = {}

    def __init__(
        self, required=False, default=None, dump_to=None, load_from=None, **kwargs
    ):
        self.required = required
        self.default = default
        self.dump_to = dump_to
        self.load_from = load_from
        self.options = kwargs

    def dumps(self, d):
        raise NotImplementedError

    def loads(self, d):
        raise NotImplementedError
