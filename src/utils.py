import yaml
import logging

logger = logging.getLogger("syslogger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)

# read config file
try:
    with open("../config.yml", "r") as file:
        config = yaml.safe_load(file)
except:
    logger.info("Error: 没有找到文件或读取文件失败")
    exit(1)


def sys_config():
    return config


def get_logger():
    return logger
