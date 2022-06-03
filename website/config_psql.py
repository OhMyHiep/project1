

from configparser import ConfigParser
import os


def config(fileName='config.ini',section='database'):
    db={}
    print(os.path.isfile(fileName))
    if os.path.isfile(fileName):
        parser=ConfigParser()
        parser.read(fileName)
        # for i in parser:
        #     print("i",i)
        if parser.has_section(section):
            params=parser.items(section)
            for param in params:
                db[param[0]]=param[1]
        else:
            raise Exception (f'(section {section} not found in {fileName})')
    else:
        raise Exception ("File Not Found") 
    return db

    