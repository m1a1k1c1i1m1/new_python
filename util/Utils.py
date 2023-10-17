import os
from loguru import logger
import hashlib
import time
import json


class Utils:

    def create_todo(self, data, name_dir):
        if self.chek_dir(name_dir):
            self.seve(data, name_dir, self.hashlib_16(data[0]))
            logger.info(f'todo create: {data[0]}')
        else:
            self.create_dir(name_dir)
            self.seve(data, name_dir,  self.hashlib_16(data[0]))
            logger.info(f'create todo: {data[0]}')

    def create_todo_phone_user(self, data, name_dir):
        if self.chek_dir(name_dir):
            self.seve_todo(data, f'{name_dir}{self.hashlib_16(data["url"])}')
            logger.info(f'todo create: {data["url"]}')
        else:
            self.create_dir(name_dir)
            self.seve_todo(data, f'{name_dir}{self.hashlib_16(data["url"])}')
            logger.info(f'create todo: {data["url"]}')

    def create_dir(self, name_dir):
        try:
            os.mkdir(name_dir)
            logger.info(f"Папка создана: {name_dir}")
        except Exception as error:
            logger.error(f'Папка с таким именем {name_dir} существует')

    def seve(self, data, name_file):
        for item in data:
            str(item)
        with open(f'{name_file}', 'w', encoding='utf-8') as File:
            File.write('_$_'.join(data))

    def seve_todo(self, data, name_file):
        data_json = json.dumps(data)
        file = json.loads(str(data_json))
        with open(f'{name_file}.json', 'w', encoding='utf-8') as File:
            json.dump(file, File, indent=4)

    def chek_dir(self, name_dir):
        if not os.path.exists(name_dir):
            return False
        else:
            return True

    def open_file(self, name_file, name_dir):
        with open(f'{name_dir}{name_file}', 'r') as File:
            file = File.read()
            logger.info(f'открыт файл : {name_file} из папки {name_dir}')
            return file

    def delet_file(self, name_file, name_dir):
        os.remove(name_file)
        logger.info(f'файл удален: {name_file} из папки {name_dir} ')

    def hashlib_16(self, str_hash):
        hash = hashlib.md5()
        hash.update(str_hash.encode('utf-8'))
        name = hash.hexdigest()
        return name

