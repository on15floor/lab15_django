import json
from datetime import datetime

import pymongo
from bson import json_util
from django.conf import settings
from django.core.exceptions import PermissionDenied


class BaseMixin:
    def __init__(self):
        self.token = ''
        self.uri = ''
        self.status = 'success'

    def check_token(self, request, token=settings.API_QUERY_TOKEN):
        if 'token' in request.GET:
            self.token = request.GET['token']
            self.uri = request.path
            if self.token == token:
                return
        self.status = 'error'
        self.save_log_to_mongodb(message='Wrong token')
        raise PermissionDenied

    def save_log_to_mongodb(self, message):
        log = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status,
            'token': self.token,
            'uri': self.uri,
            'message': message
        }
        mongodb = pymongo.MongoClient(settings.MONGO_CONN_STRING)
        database = mongodb.lab15_ru
        collection = database.api_requests
        collection.insert_one(json.loads(json_util.dumps(log)))
        return log
