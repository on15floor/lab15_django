import json

import requests


class Crontab:
    def __init__(self):
        self.login = 'fh7915ko'
        self.password = '03fe90aq'

    def url_gen(self, command) -> str:
        """ Генерирует GET ссылку
        :return: str ссылка для get запроса
        """
        return f'https://api.beget.com/api/cron/{command}?login={self.login}&passwd={self.password}&output_format=json'

    def tasks_get(self) -> list:
        """ Возвращает список задач
        :return: list of dicts
        """
        tasks = requests.get(self.url_gen('getList'))
        tasks_json = json.loads(tasks.text)
        return tasks_json['answer']['result']

    def task_del(self, task_id) -> None:
        """ Удаление задачи
        :param task_id: id задачи
        :return: None
        """
        base_url = self.url_gen('delete')
        data = {'row_number': task_id}
        requests.get(f'{base_url}&input_format=json', params={'input_data': json.dumps(data)})

    def task_change_state(self, task_id: int, state: int) -> None:
        """ Остановить/запустить задачу
        :param task_id: id задачи
        :param state: состояние задачи: 1 - остановить задачу, 0 - запустить задачу
        :return: None
        """
        base_url = self.url_gen('changeHiddenState')
        data = {'row_number': task_id,
                'is_hidden': state}
        requests.get(f'{base_url}&input_format=json', params={'input_data': json.dumps(data)})
