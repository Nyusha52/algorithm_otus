import datetime


def time_(func):
    '''
    Печатает время выполнения функции
    :param func: функция
    :return: функция
    '''

    def wrapper(*arg):
        start = datetime.datetime.now()
        result = func(*arg)
        print(datetime.datetime.now() - start)
        return result

    return wrapper
