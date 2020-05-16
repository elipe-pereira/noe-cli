#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser
from datetime import date
from pathlib import PurePath


def main():
    config = configparser.ConfigParser()
    config.read("/etc/noe/noe.conf")

    for section in config.sections():
        type_backup = config.get(section, 'type_backup')
        folder_backup = config.get(section, 'folder_backup')
        folder_dest = config.get(section, 'folder_dest')
        remote_share = config.get(section, 'remote_share')
        host = config.get(section, 'host')
        user = config.get(section, 'user')
        password = config.get(section, 'password')
        bucket_name = config.get(section, 'bucket_name')
        access_key = config.get(section, 'access_key')
        secret_access_key = config.get(section, 'secret_access_key')

        if folder_backup == "/":
            file = "full"
        else:
            file = PurePath(folder_backup).name

        filename = "{0}-{1}-{2}".format(file, section, date.today())
        exclude_list_file = config.get(section, 'exclude_list_file')

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        if type_backup == 'local':
            os.system("tar --exclude-from={0} -zcvf {1}/{2}.tar.gz {3}"
                      .format(exclude_list_file, folder_dest, filename, folder_backup))
        elif type_backup == "samba":
            ret = os.system("mount //{0}/{1} {2} -o username={3},password={4}"
                            .format(host, remote_share, folder_dest, user, password))
            print (ret)

            if ret == 1:
                print("Houve um problema na montagem do compartilhamento")
            else:
                os.system("tar --exclude-from={0} -zcvf {1}/{2}.tar.gz {3}"
                          .format(exclude_list_file, folder_dest, filename, folder_backup))
        else:
            print("Tipo de backup não válido")


if __name__ == '__main__':
    main()
