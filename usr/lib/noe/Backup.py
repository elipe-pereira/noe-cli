#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser
from .Config import Config


class Backup(object):
    def run(self, exclude_list_file, folder_dest, filename, folder_backup):
        os.system("tar --exclude-from={0} --exclude={1} -zcvf {2}/{3}.tar.gz {4}"
                  .format(exclude_list_file, folder_dest, folder_dest, filename, folder_backup))

