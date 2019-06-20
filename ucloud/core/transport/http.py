# -*- coding: utf-8 -*-

import logging
import json as json_mod

logger = logging.getLogger(__name__)


class Request(object):
    def __init__(
        self,
        url,
        method="GET",
        params=None,
        data=None,
        json=None,
        headers=None,
        **kwargs
    ):
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.json = json
        self.headers = headers


class Response(object):
    def __init__(
        self,
        url,
        method,
        request=None,
        status_code=None,
        reason=None,
        headers=None,
        content=None,
        **kwargs
    ):
        self.url = url
        self.method = method
        self.request = request
        self.status_code = status_code
        self.reason = reason
        self.headers = headers
        self.content = content

    def json(self):
        return json_mod.loads(self.content)


class Transport(object):
    """ the abstract class of transport implementation """

    def send(self, req, **options):
        raise NotImplementedError
