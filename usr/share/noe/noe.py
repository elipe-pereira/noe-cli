#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
sys.path.insert(0, "/usr/lib/noe")
from Config import Config
from Backup import Backup
from Mount import Mount
from Services import Services


def main():
    config = Config()
    backup = Backup()
    mount = Mount()
    service_config = Config()
    command_exec = Services()

    config.set_config_file("/etc/noe/noe.conf")
    config.set_config_parser()

    service_config.set_config_file('/etc/noe/services.conf')
    service_config.set_config_parser()
    
    sections = config.getSectionsConfig()
    services = service_config.getSectionsConfig()

    for service in services:
        service_config.set_enabled(service, 'enabled')
        service_config.set_backup_name(service, 'backup_name')
        service_config.set_command_stop(service, 'command_stop')
        service_config.set_command_start(service, 'command_start')
            
        enabled = service_config.get_enabled()
        backup_name = service_config.get_backup_name()
        command_stop = service_config.get_command_stop()
        command_start = sercie_config.get_command_start()
            

        if enabled == "yes":
            command_exec.stop_service(command_stop)

        else:
            continue


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


    for service in services:
        service_config.set_enabled(service, 'enabled')
        service_config.set_backup_name(service, 'backup_name')
        service_config.set_command_stop(service, 'command_stop')
        service_config.set_command_start(service, 'command_start')
            
        enabled = service_config.get_enabled()
        backup_name = service_config.get_backup_name()
        command_stop = service_config.get_command_stop()
        command_start = sercie_config.get_command_start()
            

        if enabled == "yes":
            command_exec.start_service(command_start)

        else:
            continue



if __name__ == '__main__':
    main()
