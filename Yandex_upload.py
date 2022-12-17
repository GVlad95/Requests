import requests
import os
from settings import TOKEN


def get_file_path():
    current = os.getcwd()
    folder_name = current + r'\files'
    file_paths = [os.path.join(folder_name, f) for f in os.listdir(folder_name) if
                  os.path.isfile(os.path.join(folder_name, f))]
    return file_paths


class YandexUpload:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_file(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка произошла успешно!')


if __name__ == '__main__':
    ya = YandexUpload(TOKEN)
    file_path = get_file_path()
    print(file_path)
    for path in file_path:
        name = os.path.basename(path)
        ya.upload_file(path, name)
