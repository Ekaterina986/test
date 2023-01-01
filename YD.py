import requests
from pprint import pprint

token = "AQAAAABam0qBAADLW7nPKNIYoESCtdFSi-FbtQ4"
path1 = "нетология22/курсовая работа2"


def put_directory(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content - Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': f'OAuth {token}'
               }
    response = requests.put(f'{url}?path={path}', headers=headers)
    # if res == 201:
    #     print('Папка создана успешно.')
    return response


def get_directory(path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': path}
    response = requests.get(url, headers=headers, params=params)
    return response
