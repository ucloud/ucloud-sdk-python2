# -*- coding: utf-8 -*-

import logging
import json as json_mod
from ucloud.core.transport import utils
from ucloud.core.utils.compat import str

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

    def payload(self):
        payload = (self.params or {}).copy()
        payload.update(self.data or {})
        payload.update(self.json or {})
        return payload


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
        encoding=None,
        **kwargs
    ):
        self.url = url
        self.method = method
        self.request = request
        self.status_code = status_code
        self.reason = reason
        self.headers = headers
        self.content = content
        self.encoding = encoding

    def json(self, **kwargs):
        """ json will return the bytes of content
        """
        if not self.content:
            return None
        encoding = utils.guess_json_utf(self.content)
        if encoding is not None:
            try:
                return json_mod.loads(self.content.decode(encoding), **kwargs)
            except UnicodeDecodeError:
                pass
        return json_mod.loads(self.text, **kwargs)

    @property
    def text(self):
        """ text will return the unicode string of content,
        see `requests.Response.text`
        """
        if not self.content:
            return str("")
        try:
            content = str(self.content, self.encoding, errors="replace")
        except (LookupError, TypeError):
            content = str(self.content, errors="replace")
        return content


class Transport(object):
    """ the abstract class of transport implementation """

    def send(self, req, **options):
        raise NotImplementedError
