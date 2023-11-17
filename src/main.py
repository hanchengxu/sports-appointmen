from utils import sys_config, get_logger

print("Hello, World!")

# use config
configs = sys_config()
print(configs["login"]["user"])

# use log
logger = get_logger()
logger.info("log log")
