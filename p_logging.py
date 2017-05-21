import logging

def a():
    logging.basicConfig(filename='log.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S %p',
                        level=10)

    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')
    logging.log(9, '9')
    logging.log(10, '10')

def b():
    file1_1 = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')
    fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
    file1_1.setFormatter(fmt)

    file1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')
    fmt = logging.Formatter()
    file1_2.setFormatter(fmt)

    log1 = logging.Logger('s1', level=logging.ERROR)
    log1.addHandler(file1_1)
    log1.addHandler(file1_2)

    log1.critical('123')

if __name__ == '__main__':
    b()
    