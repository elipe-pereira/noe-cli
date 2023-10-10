#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class Services(object):
    def stop_service(self, command_stop):
        os.system(command_stop)

    def start_service(self, command_start):
        os.system(command_start)
