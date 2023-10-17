from Base.base_db import Base
from util.Utils import Utils
from time import sleep

base = Base()
util = Utils()

url_api = 'https://api.av.by/offers/{}/phones'
NAME_DIR = ['page/', 'todo/']

while True:
    def get_rows_car():
        rezult = base.get_all_car()
        for item in rezult:
            id_car = item['url_car'].split('/')[-1]
            data = {
                'url': url_api.format(id_car),
                'metod': 'GET',
                'url_new': item['url_car']
            }
            util.create_todo_phone_user(data, NAME_DIR[1])


    get_rows_car()

    sleep(3600)
