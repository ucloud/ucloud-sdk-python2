# -*- coding: utf-8 -*-

import logging
import json as json_mod
from ucloud.core import exc
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
        self.request_time = 0

    def payload(self):
        payload = (self.params or {}).copy()
        payload.update(self.data or {})
        payload.update(self.json or {})
        return payload


REQUEST_UUID_HEADER_KEY = "X-UCLOUD-REQUEST-UUID"


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
        self.content = content
        self.encoding = encoding
        self.response_time = 0
        self.headers = headers or {}
        self.request_uuid = self.headers.get(REQUEST_UUID_HEADER_KEY)

    def json(self, **kwargs):
        """json will return the bytes of content"""
        if not self.content:
            return None
        try:
            return self._decode_json(**kwargs)
        except Exception as e:
            raise exc.InvalidResponseException(
                self.content, str(e), request_uuid=self.request_uuid
            )

    @property
    def text(self):
        """text will return the unicode string of content,
        see `requests.Response.text`
        """
        if not self.content:
            return str("")
        try:
            content = str(self.content, self.encoding, errors="replace")
        except (LookupError, TypeError):
            content = str(self.content, errors="replace")
        return content

    def _decode_json(self, **kwargs):
        encoding = utils.guess_json_utf(self.content)
        if encoding is not None:
            try:
                return json_mod.loads(self.content.decode(encoding), **kwargs)
            except UnicodeDecodeError:
                pass
        return json_mod.loads(self.text, **kwargs)


class SSLOption(object):
    def __init__(
        self, ssl_verify=True, ssl_cacert=None, ssl_cert=None, ssl_key=None
    ):
        self.ssl_verify = ssl_verify
        self.ssl_cacert = ssl_cacert
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key


class Transport(object):
    """ the abstract class of transport implementation """

    def send(self, req, **options):
        raise NotImplementedError
