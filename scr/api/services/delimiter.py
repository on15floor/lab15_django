from api.utils.database import SQLite3Instance
from django.conf import settings


class Delimiter:
    def __init__(self):
        db_dir = settings.BASE_DIR
        db_name = settings.DELIMITER_DB
        self.db = SQLite3Instance(db_dir, db_name)

    def get_best_scores(self, limit) -> dict:
        """Метод возвращает словарь первых limit мест"""
        res = {}
        query = self.db.select('best_scores',
                               ['user_id', 'user_name', 'best_score'],
                               where=f'ORDER BY best_score DESC LIMIT {limit}')
        for i in range(0, len(query)):
            res[i+1] = query[i]
        return res

    def save_records(self, in_data):
        """ Метод добавления рекорда
        """
        user_id = in_data['user_id']
        self.db.delete('best_scores', where=f'WHERE user_id="{user_id}"')
        self.db.insert('best_scores', in_data)
