import json
import os
import urllib3
from util.Utils import Utils
import time
from loguru import logger

util = Utils()
NAME_DIR = ['page/', 'todo/']
HEDERS = {
    "content-type": "application/json"
}


class Load:

    def __init__(self):
        self.run_load()

    def load_url(self, data):
        new_data = json.loads(data)
        post_bady = json.dumps(new_data['body'])
        req = urllib3.request(method='POST', url=new_data['url'], body=post_bady, headers=HEDERS)
        logger.info('страница скачалась №: {}'.format(new_data['body']['page']))
        content = [req.data.decode('utf-8'), 'POST']
        try:
            util.create_dir(NAME_DIR[0])
            util.seve(content, '{} {} страница'.format(NAME_DIR[0], new_data["body"]["page"]))
        except Exception as error:
            logger.error('{} возникла в функции load_url в файле loader.py'.format(error))

    def loader_api_phone(self, data):
        req = urllib3.request(method='GET', url=data['url'], headers=HEDERS)
        content = [req.data.decode('utf-8'), 'GET', data['url_new']]
        util.seve(content, '{}{}'.format(NAME_DIR[0], util.hashlib_16(data['url'])))
        return json.dumps(content)

    def run_load(self):
        while True:
            try:
                list_file = os.listdir(NAME_DIR[1])
                for item in list_file:
                    data = util.open_file(item, NAME_DIR[1])
                    new_data = json.loads(data)
                    if new_data['metod'] == 'GET':
                        self.loader_api_phone(new_data)
                    else:
                        self.load_url(data)
                    util.delet_file(NAME_DIR[1] + item, NAME_DIR[1])
                if len(list_file) == 0:
                    time.sleep(10)
            except Exception as error:
                logger.error(error)


load = Load()
