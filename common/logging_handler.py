import logging


def get_logger(
        name="root",
        file =None,
        logger_level="DEBUG",
        stream_level="DEBUG",
        file_level = "INFO",
        fmt = '%(asctime)s--%(filename)s--hanghao:%(lineno)d--%(levelname)s:%(message)s'):
    """获取到收集器"""
    logger = logging.getLogger(name)
    # 设置收集器的级别
    logger.setLevel(logger_level)

    #输出管理器
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    logger.addHandler(stream_handler)

    # 格式
    fmt = logging.Formatter(fmt)
    stream_handler.setFormatter(fmt)

    if file:
        file_handler = logging.FileHandler(file,encoding='utf-8')
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger

if __name__ == '__main__':
    logger = get_logger()
    logger.info('hello')
