# -*- coding:utf8 -*-
import logging
import logging.handlers
import os
import time
from util.utils import get_project_path

class logs:
    def __init__(self):
        self.logger = logging.getLogger('')
        self.logger.handlers.clear()
        # 设置输出的等级
        LEVELS = {
            "NOSET": logging.NOTSET,
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        logs_dir = f"{get_project_path()}/logs"
        # logs_dir = "/var/test/operation_pc_api_test/logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改Log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        log_filename = f"{timestamp}.log"
        log_filepath = os.path.join(logs_dir, log_filename)
        rotating_file_handler = logging.handlers.RotatingFileHandler(filename = log_filepath,
                                                                     maxBytes=1024 * 1024 * 50,
                                                                     backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', '%Y-%m-%d %H:%M:%S')
        rotating_file_handler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotating_file_handler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.INFO)

        # http_client.HTTPConnection.debuglevel = 1
        # requests_log = logging.getLogger("requests.packages.urllib3")

    def info(self, message):
        self.logger.info(f">>>{message}<<<")

    def debug(self, message):
        self.logger.debug(f">>>{message}<<<")

    def warning(self, message):
        self.logger.warning(f">>>{message}<<<")

    def error(self, message):
        self.logger.error(f">>>{message}<<<")