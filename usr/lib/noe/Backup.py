#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Config(object):
    def __init__(self):
        self._type = "local"
        self._folder_backup = "/"
        self._folder_dest = "/mnt/backup"
        self._remote_share = ""
        self._host = "localhost"
        self._user = "user"
        self._password = "NOPASS"
        self._bucket_name = "bucket"
        self._access_key = "noaccesskey"
        self._secret_access_key = "nosecret"
        self._file = "full"
        self._filename = "{0}-{1}-00:00:00".format(self.file, "default")
        self._exclude_list_file = "exclude_list.txt"

    def setTypeConfigBackup(self, type):
        self._type = type

    def getTypeConfigBackup(self):
        return self._type

    def setFolderConfigBackup(self, folder_backup):
        self._folder_backup = folder_backup

    def getFolderConfigBackup(self):
        return self._folder_backup

    def setFolderDestConfigBackup(self, folder_dest):
        self._folder_dest = folder_dest

    def getFolderDestConfigBackup(self):
        return self._folder_dest

    def setRemoteShareConfigBackup(self, remote_share):
        self._remote_share = remote_share

    def getRemoteShareConfigBackup(self):
        return self._remote_share

    def setUserConfigBackup(self, user):
        self._user = user

    def getUserConfigBackup(self):
        return self._user

    def setPasswordConfigBackup(self, password):
        self._password = password

    def getPasswordConfigBackup(self):
        return self._password

    def setBucketNameConfigBackup(self, bucket_name):
        self._bucket_name = bucket_name

    def getBucketNameConfigBackup(self):
        return self._bucket_name

    def setAccessKeyConfigBackup(self, access_key):
        self._access_key =  access_key

    def getAccessKeyConfigBackup(self):
        return self._access_key

    def setSecretAccessKey(self, secret_access_key):
        self._secret_access_key = secret_access_key

    def getSecretAccessKey(self):
        return self._secret_access_key





