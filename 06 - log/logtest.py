import logging


LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"


# 输出文件名称，设置显示级别,
logging.basicConfig(filename="shasa.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")




# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")

# 如果没有设置配置，输出的信息只显示>= warning 级别