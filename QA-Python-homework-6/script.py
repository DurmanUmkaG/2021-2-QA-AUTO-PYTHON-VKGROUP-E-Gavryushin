import json
import sys
from collections import Counter


def get_data_from_file(path):
    with open(path, 'r') as file:
        return list(map(lambda x: x.split(), file.readlines()))


def get_total_number_of_requests(data):
    return {'total_number_of_requests': len(data)}


def get_total_number_of_requests_by_type(data):
    return Counter(map(lambda x: x[5][1:], data))


def get_top_10_most_frequent_requests(data):
    res = sorted(Counter(map(lambda x: x[6], data)).items(), key=lambda x: x[1], reverse=True)[:10]
    return [{'url': i[0], 'number_of_requests': i[1]} for i in res]


def get_top_5_biggest_size_requests(data):
    res = sorted([i for i in data if i[8][0] == '4'], key=lambda x: int(x[9]), reverse=True)[:5]
    return [{'url': i[6], 'status_code': int(i[8]), 'request_size': int(i[9]), 'ip': i[0]} for i in res]


def get_top_5_users_by_the_number_of_requests(data):
    res = sorted(Counter(map(lambda x: x[0], [i for i in data if i[8][0] == '5'])).items(), key=lambda x: x[1],
                 reverse=True)[:5]
    return [{'ip': i[0], 'number_of_requests': i[1]} for i in res]
