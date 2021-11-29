import json
import logging
import socket

logger = logging.getLogger('test')


class HTTPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.socket.settimeout(0.1)
        self.socket.connect((self.host, self.port))

    def _request(self, method, params, data=None):
        request = f'{method} {params} HTTP/1.1\r\nHost:{self.host}\r\n'
        if data is not None:
            data = json.dumps(data)
            request += f'Content-Type: application/json\r\n' \
                       f'Content-Length: {len(data)}\r\n' \
                       f'\r\n' \
                       f'{data}'
        else:
            request += '\r\n'

        logger.info('REQUEST:\n')
        logger.info(request + '\n\n')
        self.socket.send(request.encode())

        data = self.receive_data()
        logger.info('RESPONSE')
        logger.info('\n'.join(data) + '\n\n')

        return json.loads(data[-1])

    def post_add_user(self, name, surname):
        return self._request('POST', '/add_user', data={'name': name, 'surname': surname})

    def get_user_by_name(self, name):
        return self._request('GET', f'/get_surname/{name}')

    def delete_user_by_name(self, name):
        return self._request('DELETE', f'/delete_user/{name}')


    def receive_data(self):
        total_data = []

        while True:
            try:
                data = self.socket.recv(4096)
                if data:
                    total_data.append(data.decode('utf-8'))
                else:
                    break
            except socket.timeout:
                break

        return ''.join(total_data).splitlines()

    def close_connection(self):
        self.socket.close()
