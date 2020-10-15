#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class Mail(object):
	@staticmethod
	def send(subject, mail_address):
		os.system("test -d /`whoami`/Mail || mkdir /`whoami`/Mail ")
		os.system("cat /var/log/noe.log|mutt -F /etc/noe/muttrc -s '{0}' {1}".format(subject, mail_address))
