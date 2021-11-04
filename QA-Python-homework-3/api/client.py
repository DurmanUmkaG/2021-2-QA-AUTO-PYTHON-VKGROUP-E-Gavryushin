import logging
from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 100


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:
    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password

        self.session = requests.Session()
        self.csrf_token = None

    @staticmethod
    def log_pre(url, headers, data, expected_status):
        logger.info(f'Performing request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n'
                            f'{response.text[:MAX_RESPONSE_LENGTH]}'
                            )
            elif logger.level == logging.DEBUG:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: {response.text}\n\n'
                            )
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n'
                        )

    def _request(self, method, url, headers=None, data=None, expected_status=200, jsonify=False):
        self.log_pre(url, headers, data, expected_status)

        response = self.session.request(method, url, headers=headers, data=data)

        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')

        if jsonify:
            return response.json()
