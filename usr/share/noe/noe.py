#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
sys.path.inser("0", "/usr/lib/noe")
from .Config import Config
from .Backup import Backup
from .Mount import Mount


def main():
    #config = configparser.ConfigParser()
    #config.read("/etc/noe/noe.conf")
    config = Config()
    backup = Backup()
    mount = Mount()
    sections = config.getSectionsConfig()

    for section in sections:
        config.setTypeConfig(section, 'type_backup')
        config.setFolderConfig(section, 'folder_backup')
        config.setFolderDestConfig(section, 'folder_dest')
        config.setRemoteShareConfig(section, 'remote_share')
        config.setHostConfig(section, 'host')
        config.setUserConfig(section, 'user')
        config.setPasswordConfig(section, 'password')
        config.setBucketNameConfig(section, 'bucket_name')
        config.setAccessKeyConfig(section, 'access_key')
        config.setSecretAccessKey(section, 'secret_access_key')
        config.setFileNameConfig(section, date.today())
        config.setExcludeListFile(section, 'exclude_list_file')

        type_backup = config.getTypeConfig()
        folder_backup = config.getFolderConfig()
        folder_dest = config.getFolderDestConfig()
        remote_share = config.getRemoteShareConfig()
        host = config.getHostConfig()
        user = config.getUserConfig()
        password = config.getPasswordConfig()
        bucket_name = config.getBucketNameConfig()
        access_key = config.getAccessKeyConfig()
        secret_access_key = config.getSecretAccessKey()
        filename = config.getFileNameConfig()
        exclude_list_file = config.getExcludeListFile()

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        if type_backup == "local":
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)

        elif type_backup == "samba":
            mount.mountSamba(host, remote_share, folder_dest, user, password)
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            mount.umount(folder_dest)


        elif type_backup == "bucket":
            tmp_file = "/tmp/.passwd-s3fs"
            mount.mountBucket(access_key, secret_access_key, tmp_file, bucket_name, folder_dest)
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            mount.umount(folder_dest)

        else:
            print("Tipo de backup não válido")


if __name__ == '__main__':
    main()
