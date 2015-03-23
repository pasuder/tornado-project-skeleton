import os

from tornado_project_skeleton.tools import config


pwd = os.path.dirname(os.path.abspath(__file__))
config.add_config_ini('%s/main.ini' % pwd)

if __name__ == '__main__':
    print 'Hello World!\nValue for NAME is %s.' % config.NAME
