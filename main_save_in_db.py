from Base.base_db import Base
import os
from loguru import logger
from time import sleep
from util.Utils import Utils


util = Utils()


NAME_DIR = ['page/', 'todo/', 'car/']


class Seve(Base):

    def __init__(self):
        self.run()

    def save_phone(self, data):
        if self.check_car(data[-1], 'car') == 1:
            id_car = self.get_id_car(data[-1], 'car')
            self.update_car(data, id_car)
        else:
            logger.info('нет такой записи : {} в базе данных'.format(data[-1]))

    def save_db(self, data):
        try:
            new_data = data
            if self.check(new_data[0], 'marka') == 0:
                self.insert_info_marka(new_data[0])
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data[0]))
            if self.check(new_data[1], 'model') == 0:
                id_marka = self.get_id(new_data[0], 'marka')
                self.insert_info_model(new_data[1], id_marka)
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data[1]))
            if self.check_car(new_data[8], 'car') == 0:
                self.insert_info_car(new_data)
            else:
                logger.info('запись: {} в базе данных уже есть'.format(new_data[8]))
        except Exception as error:
            logger.info('возникла ошбка: {} в функции save_db в файле main_save_in_db.py'.format(error))


    def run(self):
        try:
            while True:
                list_file = os.listdir(NAME_DIR[2])
                for item in list_file:
                        data = util.open_file(item, NAME_DIR[2]).split('_$_')
                        if len(data) == 3:
                            self.save_phone(data)
                        else:
                            self.save_db(data)
                        util.delet_file(NAME_DIR[2] + item, NAME_DIR[2])
                if len(list_file) == 0:
                    sleep(10)
        except Exception as error:
            logger.info('возникла ошбка: {} в функции run в файле main_save_in_db.py'.format(error))



save = Seve()
