import configparser

config = configparser.ConfigParser()
config.read('text.ini', encoding='utf-8')
ret = config.sections()
print(ret)

ret = config.items('section1')
print(ret)

ret = config.options('section1')
print(ret)

v = config.get('section1', 'k1')
# v = config.getint('section1', 'k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print(v)

has_sec = config.has_section('section3')
print(has_sec)

# config.add_section('section3')
# config.write(open('text.ini', 'w'))
#
# config.remove_section('section3')
# config.write(open('text.ini', 'w'))

has_opt = config.has_option('section1', 'k1')
print(has_opt)

# config.remove_option('section', 'k1')
# config.write(open('text.ini', 'w'))

config.set('section1', 'k1', '123')
config.write(open('text.ini', 'w'))
