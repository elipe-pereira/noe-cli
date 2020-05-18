#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser
from datetime import date
import usr.lib.noe.noe


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
            file = "partial"

        filename = "{0}-{1}-{2}".format(file, section, date.today())
        exclude_list_file = config.get(section, 'exclude_list_file')

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        if type_backup == "local":
            os.system("tar --exclude-from={0} --exclude={1} -zcvf {2}/{3}.tar.gz {4}"
                      .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))

        elif type_backup == "samba":
            os.system("mount //{0}/{1} {2} -o username={3},password={4} || exit 1"
                            .format(host, remote_share, folder_dest, user, password))
            os.system("tar --exclude-from={0} --exclude={1} -zcvf {2}/{3}.tar.gz {4}"
                          .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))
            os.system("umount {0}".format(folder_dest))

        elif type_backup == "bucket":
            tmp_file = "/tmp/.passwd-s3fs"

            os.system("echo {0}:{1} > {2}".format(access_key, secret_access_key, tmp_file))
            os.chmod(tmp_file, 0O600)
            os.system("s3fs {0} {1} -o passwd_file={2} -o use_path_request_style"
                      .format(bucket_name, folder_dest, tmp_file))
            os.system("tar --exclude-from={0} --exclude={1} -zcvf {2}/{3}.tar.gz {4}"
                      .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))
            os.system("umount {0}".format(folder_dest))

        else:
            print("Tipo de backup não válido")


if __name__ == '__main__':
    main()
