#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

class Log(object):
	def __init__(self):
		self.__name = "Backup"
		self.__log_file = "/var/log/noe.log"
		self.__log = logging.getLogger(self.__name)
		self.__log.setLevel(logging.DEBUG)
		self.__fh = logging.FileHandler(self.__log_file)
		self.__fh.setLevel(logging.DEBUG)
		self.__format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.__fh.setFormatter(self.__format)
		self.__log.addHandler(self.__fh)


	def get_log_file(self):
		return self.__log_file
		

	def log(self, message):
		self.__log.info(message)