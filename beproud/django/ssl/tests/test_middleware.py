#:coding=utf-8:

from django.test import TestCase as DjangoTestCase

from beproud.django.ssl.middleware import SSLProxyMiddleware
from beproud.django.ssl.tests.base import request_factory


class SSLProxyMiddlewareTest(DjangoTestCase):
    def test_secure(self):
        request = request_factory("get", "/path", X_HTTPS="ON")
        middleware = SSLProxyMiddleware(header_name="X_HTTPS", header_value="ON")

        middleware.process_request(request)

        self.assertEqual(request.is_secure(), True)
        self.assertEqual(request.build_absolute_uri(), "https://%s/path" % request.get_host())

        # NOTE: For Django 1.7+
        if hasattr(request, "scheme"):
            self.assertEqual(request.scheme, "https")
