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


def create_answer_file(data, jsonify):
    text_total_number_of_requests = 'Общее количество запросов'
    res_total_number_of_requests = get_total_number_of_requests(data)

    text_total_number_of_request_by_type = 'Общее количество запросов по типу'
    res_total_number_of_requests_by_type = get_total_number_of_requests_by_type(data)

    text_top_10_most_frequent_requests = 'Топ 10 самых частых запросов'
    res_top_10_most_frequent_requests = get_top_10_most_frequent_requests(data)

    text_top_5_biggest_size_requests = 'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ)'
    res_top_5_biggest_size_requests = get_top_5_biggest_size_requests(data)

    text_top_5_users_by_the_number_of_requests = 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой'
    res_top_5_users_by_the_number_of_requests = get_top_5_users_by_the_number_of_requests(data)

    with open('answer.txt', 'w') as file:
        print(text_total_number_of_requests, file=file)
        print(res_total_number_of_requests['total_number_of_requests'], file=file)
        print(file=file)

        print(text_total_number_of_request_by_type, file=file)
        for key, value in res_total_number_of_requests_by_type.items():
            print(key, value, file=file)
        print(file=file)

        print(text_top_10_most_frequent_requests, file=file)
        for i in res_top_10_most_frequent_requests:
            print(i['url'], i['number_of_requests'], file=file)
        print(file=file)

        print(text_top_5_biggest_size_requests, file=file)
        for i in res_top_5_biggest_size_requests:
            print(i['url'], i['status_code'], i['request_size'], i['ip'], file=file)
        print(file=file)

        print(text_top_5_users_by_the_number_of_requests, file=file)
        for i in res_top_5_users_by_the_number_of_requests:
            print(i['ip'], i['number_of_requests'], file=file)

    if jsonify:
        with open('answer.json', 'w', encoding='utf8') as file:
            json.dump(
                {
                    text_total_number_of_requests: res_total_number_of_requests,
                    text_total_number_of_request_by_type: res_total_number_of_requests_by_type,
                    text_top_10_most_frequent_requests: res_top_10_most_frequent_requests,
                    text_top_5_biggest_size_requests: res_top_5_biggest_size_requests,
                    text_top_5_users_by_the_number_of_requests: res_top_5_users_by_the_number_of_requests
                },
                file,
                indent=4,
                ensure_ascii=False
            )


if __name__ == '__main__':
    path = [arg for arg in sys.argv if 'access.log' in arg][0]
    jsonify = True if '--json' in sys.argv else False
    create_answer_file(get_data_from_file(path), jsonify=jsonify)
