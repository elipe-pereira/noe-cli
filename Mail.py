#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class Mail(object):
	@staticmethod
	def send(subject, mail_address):
		os.system("cat /var/log/noe.log|mutt -s '{0}' {1}".format(subject, mail_address))
