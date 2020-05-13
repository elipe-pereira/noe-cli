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
        folder_dest = config.get(section, 'folder_dest')
        folder_backup = config.get(section, 'folder_backup')
        type_backup = config.get(section, 'type_backup')
        file = PurePath(folder_backup).name
        filename = "{0}-{1}-{2}".format(file, section, date.today())

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        if type_backup == 'local':
            os.system("tar -zcvf {0}/{1}.tar.gz {2}".format(folder_dest, filename, folder_backup))


if __name__ == '__main__':
    main()
