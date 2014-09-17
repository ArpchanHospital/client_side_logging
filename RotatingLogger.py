import logging
import logging.config
import yaml


class RotatingLogger:
    def __init__(self, config_file, logger_name):
        config_file_dict = yaml.load(open(config_file, 'r'))
        logging.config.dictConfig(config_file_dict)
        self.log = logging.getLogger(logger_name)