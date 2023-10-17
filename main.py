import time
from util.Utils import Utils
from Base.base_db import Base

util = Utils()
base = Base()


while True:

    def create_todo():
        url = 'https://api.av.by/offer-types/cars/filters/main/apply'
        name_dir = 'todo/'
        body = {
            "page": 1,
            "properties": [
                {
                    "name": "price_currency",
                    "value": 2
                }
            ],
            "sorting": 1
        }  # body content
        data = {
            'url': url,
            'body': body,
            'metod': 'POST'
        }  # данные для POST запроса
        while body['page'] <= 50:
            if not util.chek_dir(name_dir):
                util.create_dir(name_dir)
            util.seve_todo(data, name_dir + '{} страница'.format(body["page"]))
            body['page'] += 1



    create_todo()

    time.sleep(3600)
