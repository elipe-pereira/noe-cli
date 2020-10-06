## Backup e recovery


## Ferramenta de backup:

 - Noe

## Arquivo de configuração:

 - /etc/noe/noe.conf


## Comando

O backup é todo parametrizado no arquivo de configuração /etc/noe/noe.conf.

Após configurado, basta executar o comando:

    # noe


o backup será executado e os arquivos que foram copiados e comprimidos aparecerão na tela via linha de comando.

Para agendar uma vez por semana o backup, foi utilizado o programa cron, ao qual, um dos arquivos de configuração é o arquivo /etc/crontab

A configuração efetuada foi a seguinte:


    00 01   * * 7 root /usr/bin/noe

>


A ordem de datas é a seguinte:

Primeiro campo equivale a minutos, segundo campo equivale a horas, 3 campo em asterisco equivale a dia do mês, 4º campo em asterisco equivale ao mês do ano e o último campo com o valor 7 equivale ao dia semana em que será executado. 7 equivale ao dia de domingo.

Ou seja:

o backup executará todo domingo às 01:00 da madrugada em qualquer dia do mês e qualquer mês do ano.


## Configuração do backup

    [DEFAULT]
    mail_address =
    enable_stop_services = no
    command_services_stop = systemctl stop syslog
    command_services_start = systemctl start syslog

    [backup-full]
    type_backup = local-sync-onedrive
    folder_dest = /root/OneDrive/lgpdcanaldotitular/backup_offsite_DO
    folder_backup = /
    time_keep = 30d
    remote_share =
    host =
    user =
    password =
    database =
    exclude_list_file = /etc/noe/exclude_list.txt
    bucket_name =
    access_key =
    secret_access_key =
>

Os backups são divididos em seções, cada seção tem o nome cercado por colchetes. Podem haver inúmeras seções de backup e elas serão executadas sequencilamente de cima para baixo. A Seção [DEFAULT] define alguns parâmetros que devem ser iguais em todas as configurações de backup.

O ideal é nomear cada seção de backup de acordo com o tipo de cópia do sistema que você pretende fazer:

Por exemplo, nessa configuração foi nomeada como backup-full. Na configuração podemos ver que o parâmetro folder_backup é barra (/). Ou seja, será feito o backup de todo o sistema de arquivos.

Então se você for fazer o backup da pasta /home, é interessante que você identifique isso no nome da seção, por exemplo, [backup-home].

O arquivo compactado gerado pelo noe no backup terá o nome da seção + dia do ano. Por exemplo, backup-full-2020-08-20.tar.gz .

O noe possui suporte a sincronização via upload para a nuvem OneDrive da Microsoft. Então se você deseja sincronizar seu backup com a nuvem, você deve colocar o parâmetro type_backup = local-sync-onedrive e o parâmetro folder_dest (Pasta destino do backup) precisa estar apontando para um pasta dentro de /root/OneDrive porque essa é a pasta default de sincronização.

## Backup via Samba

    [DEFAULT]
    mail_address =
    enable_stop_services = no
    command_services_stop = systemctl stop syslog
    command_services_start = systemctl start syslog

    [backup-full]
    type_backup = samba
    folder_dest = /mnt/backup
    folder_backup = /
    time_keep = 30d
    remote_share = backup
    host = 192.168.1.200
    user = test
    password = test
    database =
    exclude_list_file = /etc/noe/exclude_list.txt
    bucket_name =
    access_key =
    secret_access_key =


Em backups via samba, os campos remote_share, host, user e password devem ser preenchidos adequadamente para que a montagem do compartilhamento samba possa ser efetuado adequadamente. A pasta definida em folder_dest deverá ser uma pasta válida e será nela que o compartilhamento será montado.

Os parametros command_services_stop e command_services_start, são comandos para definir a parada de alguns serviços durante o backup caso o usuário desejar. Esses comandos devem obrigatoriamente ser separados por vírgula.

O parametro type_backup é quem define que tipo de backup será e de acordo com o tipo, alguns parametros precisam ser preenchidos e outros podem ser deixados em branco.

## Backup Local

    [DEFAULT]
    mail_address =
    enable_stop_services = no
    command_services_stop = systemctl stop syslog
    command_services_start = systemctl start syslog

    [backup-full]
    type_backup = local
    folder_dest = /mnt/backup
    folder_backup = /
    time_keep = 30d
    remote_share = backup
    host =
    user = test
    password = test
    database =
    exclude_list_file = /etc/noe/exclude_list.txt
    bucket_name =
    access_key =
    secret_access_key =


Com o backup do tipo local (type_backup = local), você somente precisará informar folder_dest ou seja, onde será armazenado o backup e o folder_backup que é a pasta que será copiada e compactada no backup.


## Backup Bucket AWS

    [DEFAULT]
    mail_address =
    enable_stop_services = no
    command_services_stop = systemctl stop syslog
    command_services_start = systemctl start syslog

    [backup-full]
    type_backup = bucket
    folder_dest = /mnt/backup
    folder_backup = /
    time_keep = 30d
    remote_share = backup
    host =
    user = test
    password = test
    database =
    exclude_list_file = /etc/noe/exclude_list.txt
    bucket_name = meubucket
    access_key = acesskey
    secret_access_key = secrekeyaws


O backup do tipo bucket, irá montar um compartilhamento via s3fs com o bucket da Amazon AWS. Você precisará informar o nome do bucket que será montado em folder_dest, o access_key e secret_access_key. Caso o nome do bucket, access_key e secret_access_key estejam corretos, o backup ocorrerá normalmente.

## Backup MySQL

    [DEFAULT]
    mail_address =
    enable_stop_services = no
    command_services_stop = systemctl stop syslog
    command_services_start = systemctl start syslog

    [backup-db-xxx-mysql]
    type_backup = mysql
    folder_dest = /mnt/backup
    folder_backup =
    time_keep = 30d
    remote_share = backup
    host = localhost
    user = test
    password = test
    database =
    exclude_list_file = /etc/noe/exclude_list.txt
    bucket_name =
    access_key =
    secret_access_key =

O tipo de backup mysql, você precisará informar a pasta de destino folder_dest, host, user, password e database que você quer fazer o backup. Para cada base de dados é necessário uma configuração em uma nova seção.
