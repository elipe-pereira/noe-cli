#!/usr/bin/python3
# coding: utf-8

import logging


class Log:
    def __init__(self):
        self.name = "Backup"
        self.log_file = "/var/log/noe.log"
        self.log = logging.getLogger(self.name)
        self.log.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler(self.log_file)
        self.fh.setLevel(logging.DEBUG)
        self.format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
        self.fh.setFormatter(self.format)
        self.log.addHandler(self.fh)

    def get_log_file(self):
        return self.log_file

    def log(self, message):
        self.log.info(message)
