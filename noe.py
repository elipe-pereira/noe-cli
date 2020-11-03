#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from datetime import date
from config.Config import Config
from backup import Backup
from mount import Mount
from services import Services
from log import Log
from mail import Mail


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

    local_sync_onedrive_flag = 0
    send_file_onedrive_flag = 0

    log.log("Iniciando backup")

    config.set_enable_stop_services('DEFAULT', 'enable_stop_services')
    config.set_command_stop('DEFAULT', 'command_services_stop')
    config.set_command_start('DEFAULT', 'command_services_start')

    enable_stop_services = config.get_enable_stop_services()
    command_stop = config.get_command_stop().split(',')
    command_start = config.get_command_start().split(',')

    if enable_stop_services == "yes":
        log.log("Parando serviços")
        for command in command_stop:
            command_exec.stop_service(command)

    for section in sections:
        if section == 'DEFAULT':
            continue

        log.log("Executando backup: " + section)
        config.set_type_config(section, 'type_backup')
        config.set_folder_config(section, 'folder_backup')
        config.set_folder_dest_config(section, 'folder_dest')
        config.set_time_keep(section, 'time_keep')
        config.set_remote_share_config(section, 'remote_share')
        config.set_host_config(section, 'host')
        config.set_user_config(section, 'user')
        config.set_password_config(section, 'password')
        config.set_database(section, 'database')
        config.set_bucket_name_config(section, 'bucket_name')
        config.set_access_key_config(section, 'access_key')
        config.set_secret_access_key(section, 'secret_access_key')
        config.set_file_name_config(section, date.today())
        config.set_exclude_list_file(section, 'exclude_list_file')

        type_backup = config.get_type_config()
        folder_backup = config.get_folder_config()
        folder_dest = config.get_folder_dest_config()
        time_keep = config.get_time_keep()
        remote_share = config.get_remote_share_config()
        host = config.get_host_config()
        user = config.get_user_config()
        password = config.get_password_config()
        database = config.get_database()
        bucket_name = config.get_bucket_name_config()
        access_key = config.get_access_key_config()
        secret_access_key = config.get_secret_access_key()
        filename = config.get_file_name_config()
        exclude_list_file = config.get_exclude_list_file()

        if not os.path.isdir(folder_dest):
            os.mkdir(folder_dest)

        os.system("tmpreaper {0} {1}".format(time_keep, folder_dest))

        if type_backup == "local":
            log.log("Backup do tipo local")
            log.log("Executando cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup " + section)

        elif type_backup == "local-sync-onedrive":
            log.log("Backup do tipo local-sync-onedrive")
            log.log("Executando a cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup " + section)

            local_sync_onedrive_flag = 1

        elif type_backup == "send-file-onedrive":
            log.log("Backup do tipo send-file-onedrive")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup " + section)

            send_file_onedrive_flag = 1

        elif type_backup == "samba":
            log.log("Executando backup do tipo samba")
            log.log("Montando compartilhamento")
            mount.mountSamba(host, remote_share, folder_dest, user, password)
            log.log("Executando cópia e compressão dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Fim do backup " + section)
            log.log("Desmontando compartilhamento")
            mount.umount(folder_dest)

        elif type_backup == "bucket":
            tmp_file = "/tmp/.passwd-s3fs"
            log.log("Montando o bucket")
            mount.mountBucket(access_key, secret_access_key, tmp_file, bucket_name, folder_dest)
            log.log("Executando a cópia e compactação dos arquivos")
            backup.run(exclude_list_file, folder_dest, filename, folder_backup)
            log.log("Demontando bucket")
            mount.umount(folder_dest)

        elif type_backup == "mysql":
            log.log("Executando backup do banco de dados")
            os.system("mysqldump -u {0} -p{1} {2} -h {3} > {4}/{5}.sql".format(
                user,
                password,
                database,
                host,
                folder_dest,
                filename
            ))
            os.system("tar -zcvf {0}/{1}.tar.gz {0}/{1}.sql".format(folder_dest, filename))
            os.system("rm {0}/{1}.sql".format(folder_dest, filename))
            log.log("Backup do banco de dados concluído")

        else:
            print("Tipo de backup não válido")

    if enable_stop_services == "yes":
        log.log("Subindo serviços")
        for command in command_start:
            command_exec.start_service(command)

    if local_sync_onedrive_flag == 1:
        log.log("Sincronizando pasta de backup com a nuvem")
        folder_sync_onedrive = os.path.basename(folder_dest)
        os.system("onedrive --synchronize --upload-only --no-remote-delete")
        os.system("onedrive --synchronize --single-directory '{0}'".format(folder_sync_onedrive))
        log.log("Envio concluído")

    elif send_file_onedrive_flag == 1:
        log.log("Enviando backup via upload para o onedrive")
        os.system("onedrive --synchronize --upload-only --no-remote-delete")
        log.log("Envio concluído")


    config.set_mail_address('DEFAULT', 'mail_address')
    mail_address = config.get_mail_address()

    log.log("Enviando E-mail")
    mail.send("Backup NOE", mail_address)


if __name__ == '__main__':
    main()
