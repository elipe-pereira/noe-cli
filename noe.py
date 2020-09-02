#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
from config.Config import Config
from Backup import Backup
from Mount import Mount
from Services import Services
from Log import Log
from Mail import Mail


def main():
    main_file_exec_path = os.path.realpath(sys.argv[0])
    working_dir = os.path.dirname(main_file_exec_path)
    config_file = working_dir + "/config/noe/noe.conf"
    
    config = Config(config_file)
    backup = Backup()
    mount = Mount()
    command_exec = Services()
    log = Log()
    mail = Mail()

    sections = config.get_sections_config()
    log_file = log.get_log_file()

    os.system("echo > {0}".format(log_file))

    log.log("Iniciando backup")
    for section in sections:
        log.log("Executando backup: " + section)
        config.set_type_config(section, 'type_backup')
        config.set_folder_config(section, 'folder_backup')
        config.set_folder_dest_config(section, 'folder_dest')
        config.set_time_keep(section, 'time_keep')
        config.set_remote_share_config(section, 'remote_share')
        config.set_host_config(section, 'host')
        config.set_user_config(section, 'user')
        config.set_password_config(section, 'password')
        config.set_bucket_name_config(section, 'bucket_name')
        config.set_access_key_config(section, 'access_key')
        config.set_secret_access_key(section, 'secret_access_key')
        config.set_file_name_config(section, date.today())
        config.set_exclude_list_file(section, 'exclude_list_file')
        config.set_enable_stop_services(section, 'enable_stop_services')
        config.set_command_stop(section, 'command_services_stop')
        config.set_command_start(section, 'command_services_start')
        config.set_mail_address(section, 'mail_address')

        type_backup = config.get_type_config()
        folder_backup = config.get_folder_config()
        folder_dest = config.get_folder_dest_config()
        time_keep = config.get_time_keep()
        remote_share = config.get_remote_share_config()
        host = config.get_host_config()
        user = config.get_user_config()
        password = config.get_password_config()
        bucket_name = config.get_bucket_name_config()
        access_key = config.get_access_key_config()
        secret_access_key = config.get_secret_access_key()
        filename = config.get_file_name_config()
        exclude_list_file = config.get_exclude_list_file()
        enable_stop_services = config.get_enable_stop_services()
        command_stop = config.get_command_stop().split(',')
        command_start = config.get_command_start().split(',')
        mail_address = config.get_mail_address()

        if enable_stop_services == "yes":
            log.log("Parando serviços")
            for command in command_stop:
                command_exec.stop_service(command)

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        os.system("tmpwatch {0} {1}".format(time_keep, folder_dest))

        if type_backup == "local":
            log.log("Backup do tipo local")
            log.log("Executando cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup " + section)

        elif type_backup == "local-sync-onedrive":
            log.log("Backup do tipo local-sync-onedrive")
            log.log("Executando a cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup" + section)
            log.log("Sincronizando com a nuvem")
            os.system("onedrive --synchronize --upload-only --no-remote-delete")
            log.log("Envio concluído")

        elif type_backup == "samba":
            log.log("Executando backup do tipo samba")
            log.log("Montando compartilhamento")
            mount.mountSamba(host, remote_share, folder_dest, user, password)
            log.log("Executando cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Desmontando compartilhamento")
            mount.umount(folder_dest)

        elif type_backup == "bucket":
            tmp_file = "/tmp/.passwd-s3fs"
            mount.mountBucket(access_key, secret_access_key, tmp_file, bucket_name, folder_dest)
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            mount.umount(folder_dest)

        else:
            print("Tipo de backup não válido")

        if enable_stop_services == "yes":
            log.log("Subindo serviços")
            for command in command_start:
                command_exec.start_service(command)

        log.log("Enviando E-mail")
        mail.send("Backup NOE", mail_address)


if __name__ == '__main__':
    main()
