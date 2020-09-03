#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from datetime import date


class Config(object):
    def __init__(self, config_file):
        self.__config_file = config_file
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__config_file)
        self.__sections_config = self.__config.sections()
        self.__type_backup = "local"
        self.__folder_backup = "/"
        self.__folder_dest = "/mnt/backup"
        self.__time_keep = "10d"
        self.__remote_share = ""
        self.__host = "localhost"
        self.__user = "user"
        self.__password = "NOPASS"
        self.__database = " "
        self.__bucket_name = "bucket"
        self.__access_key = "noaccesskey"
        self.__secret_access_key = "nosecret"
        self.__filename = "{0}-00:00:00".format("default")
        self.__exclude_list_file = "exclude_list.txt"
        self.__mail_address = ""
        self.__enable_stop_services = ""
        self.__command_stop = ""
        self.__command_start = ""

    def get_sections_config(self):
        return self.__sections_config

    def set_type_config(self, section, type_backup):
        self.__type_backup = self.__config.get(section, type_backup)

    def get_type_config(self):
        return self.__type_backup

    def set_folder_config(self, section, folder_backup):
        self.__folder_backup = self.__config.get(section, folder_backup)

    def get_folder_config(self):
        return self.__folder_backup

    def set_folder_dest_config(self, section, folder_dest):
        self.__folder_dest = self.__config.get(section, folder_dest)

    def get_folder_dest_config(self):
        return self.__folder_dest

    def set_time_keep(self, section, set_time_keep):
        self.__time_keep = self.__config.get(section, set_time_keep)

    def get_time_keep(self):
        return self.__time_keep

    def set_remote_share_config(self, section, remote_share):
        self.__remote_share = self.__config.get(section, remote_share)

    def get_remote_share_config(self):
        return self.__remote_share

    def set_host_config(self, section, host):
        self.__host = self.__config.get(section, host)

    def get_host_config(self):
        return self.__host

    def set_user_config(self, section, user):
        self.__user = self.__config.get(section, user)

    def get_user_config(self):
        return self.__user

    def set_password_config(self, section, password):
        self.__password = self.__config.get(section, password)

    def get_password_config(self):
        return self.__password

    def set_database(self, section, database):
        self.__database = self.__config.get(section, database)

    def get_database(self):
        return self.__database

    def set_bucket_name_config(self, section, bucket_name):
        self.__bucket_name = self.__config.get(section, bucket_name)

    def get_bucket_name_config(self):
        return self.__bucket_name

    def set_access_key_config(self, section, access_key):
        self.__access_key = self.__config.get(section, access_key)

    def get_access_key_config(self):
        return self.__access_key

    def set_secret_access_key(self, section, secret_access_key):
        self.__secret_access_key = self.__config.get(section, secret_access_key)

    def get_secret_access_key(self):
        return self.__secret_access_key

    def set_file_name_config(self, section, date):
        self.__filename = "{0}-{1}".format(section, date)

    def get_file_name_config(self):
        return self.__filename

    def set_exclude_list_file(self, section, exclude_list_file):
        self.__exclude_list_file = self.__config.get(section, exclude_list_file)

    def get_exclude_list_file(self):
        return self.__exclude_list_file

    def set_mail_address(self, section, mail_address):
        self.__mail_address = self.__config.get(section, mail_address)

    def get_mail_address(self):
        return self.__mail_address

    def set_enable_stop_services(self, section,  enable_stop_services):
        self.__enable_stop_services = self.__config.get(section, enable_stop_services)

    def get_enable_stop_services(self):
        return self.__enable_stop_services

    def set_command_stop(self, section, command_stop):
        self.__command_stop = self.__config.get(section, command_stop)

    def get_command_stop(self):
        return self.__command_stop

    def set_command_start(self, section, command_start):
        self.__command_start = self.__config.get(section, command_start)

    def get_command_start(self):
        return self.__command_start
