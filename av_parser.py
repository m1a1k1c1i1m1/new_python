import json
import os
from loguru import logger
from util.Utils import Utils
import time

NAME_DIR = ['page/', 'todo/', 'car/']
util = Utils()


class Parser:

    def __init__(self):
        self.loop()

    def pars_phone(self, data):
        try:
            cod_phone = json.loads(data[0])[0]["country"]['code']
            number = json.loads(data[0])[0]["number"]
            new_data = data[-1]
            save_data = [cod_phone, number, new_data]
            util.seve(save_data, '{}{}'.format(NAME_DIR[2], util.hashlib_16(new_data)))
        except Exception as error:
            logger.info('возникла ошибка: {}{} в функции pars_phone'.format(error, data[0]))
            save_data = ['not', 'phone', new_data]
            util.seve(save_data, '{}{}'.format(NAME_DIR[2], util.hashlib_16(new_data)))
    def pars_car(self, data):
        new_json = json.loads(data[0])
        # data = json.loads(new_json)
        try:
            car = new_json['adverts']
            for item in car:
                name = item['properties'][0]['value']
                model = item['properties'][1]['value']
                for items in item['properties']:
                    match items['name']:
                        case 'engine_type':
                            engine_type = items['value']
                        case 'transmission_type':
                            transmission_type = items['value']
                        case 'color':
                            color = items['value']
                        case 'drive_type':
                            drive_type = items['value']
                        case 'engine_capacity':
                            engine_capacity = float(items['value'])

                new_data = [name, model, str(engine_type), str(float(0)) if engine_type == 'электро' else str(engine_capacity),
                            str(transmission_type), drive_type, color, str(item['year']), item['publicUrl'],
                            item['locationName'], str(item['publishedAt']),
                            str(item['refreshedAt']), str(item['price']['usd']['amount']),
                            str(item['price']['byn']['amount']),
                            'автосолон' if len(item['sellerName']) > 10 else item['sellerName']
                ]
                if not util.chek_dir(NAME_DIR[2]):
                    util.create_dir(NAME_DIR[2])
                    util.seve(new_data, '{}{}'.format(NAME_DIR[2], util.hashlib_16('{}{}'.format(name, str(item['price']['byn']['amount'])))))
                else:
                    util.seve(new_data, '{}{}'.format(NAME_DIR[2], util.hashlib_16('{}{}'.format(name, str(item['price']['byn']['amount'])))))
        except Exception as error:
            logger.info('возникла ошибка {} в функции pars_car'.format(error))

    def loop(self):
        try:
            while True:
                list_file = os.listdir(NAME_DIR[0])
                for item in list_file:
                    data = util.open_file(item, NAME_DIR[0])
                    new_data = data.split('_$_')
                    if new_data[1] == 'GET':
                        self.pars_phone(new_data)
                    else:
                        self.pars_car(new_data)
                    util.delet_file(NAME_DIR[0] + item, NAME_DIR[0])
                if len(list_file) == 0:
                    time.sleep(10)
        except Exception as error:
            logger.info('возниклв ошибка: {} в функции loop'.format(error))


pars = Parser()
