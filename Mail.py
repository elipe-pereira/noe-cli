#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class Mail(object):
	@staticmethod
	def send(subject, mail_address):
		os.system("mkdir /`whoami`/Mail ")
		file = open("{0}/{1}".format("/tmp", ".muttrc_tmp"), "+w")
		file.write("set use_from=yes\n")
		file.write("set mbox=+Inbox\n")
		file.write("set spoolfile=+Inbox\n")
		file.write("set envelope_from_address='noe@hanokh.com.br'\n")
		file.write("set from='noe@hanokh.com.br'\n")
		file.write("set force_name=yes\n")
		file.write("set realname='NOE'\n")
		file.write("set my_user=noe@hanokh.com.br\n")
		file.write("set my_pass='dhDe(eEP96#1JO'\n")
		file.write("set smtp_url=smtp://$my_user:$my_pass@mail.hanokh.com.br:587\n")
		file.close()
		os.system("cat /var/log/noe.log|mutt -F /tmp/.muttrc_tmp -s '{0}' {1}".format(subject, mail_address))
