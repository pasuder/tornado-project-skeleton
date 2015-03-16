from python_project_skeleton.tools import config

config.add_config_ini('main.ini')

if __name__ == '__main__':
    print 'Hello World!\nValue for NAME is %s.' % config.NAME
