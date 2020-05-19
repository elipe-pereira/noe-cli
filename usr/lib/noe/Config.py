#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
from datetime import date


class Config(object):
    def __init__(self):
        self._config_file = "/etc/noe/noe.conf"
        self._config = configparser.ConfigParser()
        self._config.read(self._config_file)
        self._sections_config = self._config.sections()
        self._type_backup = "local"
        self._folder_backup = "/"
        self._folder_dest = "/mnt/backup"
        self._remote_share = ""
        self._host = "localhost"
        self._user = "user"
        self._password = "NOPASS"
        self._bucket_name = "bucket"
        self._access_key = "noaccesskey"
        self._secret_access_key = "nosecret"
        self._filename = "{0}-00:00:00".format("default")
        self._exclude_list_file = "exclude_list.txt"

    def getSectionsConfig(self):
        return self._sections_config

    def setTypeConfig(self, section, type_backup):
        self._type_backup = self._config.get(section, type_backup)

    def getTypeConfig(self):
        return self._type_backup

    def setFolderConfig(self, section, folder_backup):
        self._folder_backup = self._config.get(section, folder_backup)

    def getFolderConfig(self):
        return self._folder_backup

    def setFolderDestConfig(self, section, folder_dest):
        self._folder_dest = self._config.get(section, folder_dest)

    def getFolderDestConfig(self):
        return self._folder_dest

    def setRemoteShareConfig(self, section, remote_share):
        self._remote_share = self._config.get(section, remote_share)

    def getRemoteShareConfig(self):
        return self._remote_share

    def setHostConfig(self, host):
        self._host = host

    def getHostConfig(self):
        return self._host

    def setUserConfig(self, section, user):
        self._user = self._config.get(section, user)

    def getUserConfig(self):
        return self._user

    def setPasswordConfig(self, section, password):
        self._password = self._config.get(section, password)

    def getPasswordConfig(self):
        return self._password

    def setBucketNameConfig(self, section, bucket_name):
        self._bucket_name = self._config.get(section, bucket_name)

    def getBucketNameConfig(self):
        return self._bucket_name

    def setAccessKeyConfig(self, section, access_key):
        self._access_key = self._config.get(section, access_key)

    def getAccessKeyConfig(self):
        return self._access_key

    def setSecretAccessKey(self, section, secret_access_key):
        self._secret_access_key = self._config.get(section, secret_access_key)

    def getSecretAccessKey(self):
        return self._secret_access_key

    def setFileNameConfig(self, section, date):
        self._filename = "{0}-{1}".format(section, date)

    def getFileNameConfig(self):
        return self._filename

    def setExcludeListFile(self, section, exclude_list_file):
        self._exclude_list_file = self._config.get(section, exclude_list_file)

    def getExcludeListFile(self):
        return self._exclude_list_file


