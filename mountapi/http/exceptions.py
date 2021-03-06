from mountapi.http import status as http_status


class HttpError(Exception):
    DEFAULT_MESSAGE = 'An error has occurred.'

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE


class HttpClientError(HttpError):
    status: dict


class Http400(HttpClientError):
    status: dict = http_status.HTTP_400_BAD_REQUEST


class Http401(HttpClientError):
    status: dict = http_status.HTTP_401_UNAUTHORIZED


class Http402(HttpClientError):
    status: dict = http_status.HTTP_402_PAYMENT_REQUIRED


class Http403(HttpClientError):
    status: dict = http_status.HTTP_403_FORBIDDEN


class Http404(HttpClientError):
    status: dict = http_status.HTTP_404_NOT_FOUND
