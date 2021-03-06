from launchkey import LAUNCHKEY_PRODUCTION
from .base import APIResponse, APIErrorResponse
import requests


class RequestsTransport(object):
    """
    Transport class for performing HTTP based queries using the requests library.
    """

    url = LAUNCHKEY_PRODUCTION
    testing = False
    verify_ssl = True

    def __init__(self):
        self._session = requests.session()

    def set_url(self, url, testing):
        """
        :param url: Base url for the querying LaunchKey API
        :param testing: Boolean stating whether testing mode is being performed. This will determine whether SSL should
        be verified.
        """
        self.url = url
        self.testing = testing
        self.verify_ssl = not self.testing

    @staticmethod
    def _parse_response(response):
        try:
            data = response.json()
        except ValueError:
            data = response.text

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if response.status_code < 500:
                return APIErrorResponse(data, response.headers, response.status_code, response.reason, response.text)
            else:
                raise

        return APIResponse(data, response.headers, response.status_code, raw_data=response.text)

    def get(self, path, headers=None, data=None):
        """
        Performs an HTTP GET request against the LaunchKey API
        :param path: Path or endpoint that will be hit
        :param headers: Headers to add onto the request
        :param data: Dictionary or bytes to be sent in the query string for the request.
        :return:
        """
        response = self._session.get(self.url + path, params=data, headers=headers, verify=self.verify_ssl)
        return self._parse_response(response)

    def post(self, path, headers=None, data=None):
        """
        Performs and HTTP POST request against the LaunchKey API
        :param path: Path or endpoint that will be hit
        :param headers: Headers to add onto the request
        :param data: Dictionary, bytes, or file-like object to send in the body of the request.
        :return:
        """
        response = self._session.post(self.url + path, data=data, headers=headers, verify=self.verify_ssl)
        return self._parse_response(response)

    def put(self, path, headers=None, data=None):
        """
        Performs and HTTP PUT request against the LaunchKey API
        :param path: Path or endpoint that will be hit
        :param headers: Headers to add onto the request
        :param data: Dictionary, bytes, or file-like object to send in the body of the request.
        :return:
        """
        response = self._session.put(self.url + path, data=data, headers=headers, verify=self.verify_ssl)
        return self._parse_response(response)

    def delete(self, path, headers=None, data=None):
        """
        Performs and HTTP DELETE request against the LaunchKey API
        :param path: Path or endpoint that will be hit
        :param headers: Headers to add onto the request
        :param data: Dictionary, bytes, or file-like object to send in the body of the request.
        :return:
        """
        response = self._session.delete(self.url + path, data=data, headers=headers, verify=self.verify_ssl)
        return self._parse_response(response)
            
    def patch(self, path, headers=None, data=None):
        """
        Performs and HTTP PATCH request against the LaunchKey API
        :param path: Path or endpoint that will be hit
        :param headers: Headers to add onto the request
        :param data: Dictionary, bytes, or file-like object to send in the body of the request.
        :return:
        """
        response = self._session.patch(self.url + path, data=data, headers=headers, verify=self.verify_ssl)
        return self._parse_response(response)
