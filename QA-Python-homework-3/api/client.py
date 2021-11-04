import logging
from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 100
LEFT = 365
RIGHT = 0


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

    def _request(self, method, url, headers=None, data=None, json_data=None, allow_redirects=True, expected_status=200,
                 jsonify=False):
        self.log_pre(url, headers, data, expected_status)

        response = self.session.request(method, url, headers=headers, data=data, json=json_data,
                                        allow_redirects=allow_redirects)

        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')

        if jsonify:
            return response.json()

        return response

    def get_csrf_token(self):
        return self._request('GET', 'https://target.my.com/csrf/')

    def post_login(self):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        response = self._request('POST', location, headers=headers, data=data)

        self.csrf_token = self.get_csrf_token().headers['set-cookie'].split(';')[0].split('=')[-1]

        return response

    def post_create_segment(self, name):
        url = urljoin(self.base_url, 'api/v2/remarketing/segments.json')

        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.csrf_token
        }

        data = {
            'logicType': 'or',
            'name': name,
            'pass_condition': 1,
            'relations': [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": LEFT,
                        "right": RIGHT
                    }
                }
            ]
        }

        resp = self._request('POST', url, headers=headers, json_data=data, jsonify=True)

        return resp

    def get_segments(self):
        url = urljoin(self.base_url, 'api/v2/remarketing/segments.json')
        response = self._request('GET', url, jsonify=True)
        return response

    def post_delete_segments(self, segment_id):
        url = urljoin(self.base_url, 'api/v1/remarketing/mass_action/delete.json')

        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.csrf_token
        }

        data = [{
            'source_id': segment_id,
            'source_type': 'segment'
        }]

        response = self._request('POST', url, headers=headers, json_data=data, jsonify=True)

        return response
