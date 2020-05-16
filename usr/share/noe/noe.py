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

        if folder_dest == "/":
            file = "root"
        else:
            file = PurePath(folder_backup).name

        filename = "{0}-{1}-{2}".format(file, section, date.today())
        exclude_list_file = config.get(section, 'exclude_list_file')

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        if type_backup == 'local':
            os.system("tar --exclude-from={0} -zcvf {1}/{2}.tar.gz {3}"
                      .format(exclude_list_file, folder_dest, filename, folder_backup))


if __name__ == '__main__':
    main()
