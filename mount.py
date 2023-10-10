#!/usr/bin/env python3
# coding: utf-8

import os


class Mount:
    def mountSamba(self, host, remote_share, folder_dest, user, password):
        os.system("mount //{0}/{1} {2} -o username={3},password={4} || exit 1"
                  .format(host, remote_share, folder_dest, user, password))

    def mountBucket(self, access_key, secret_access_key, tmp_file, bucket_name, folder_dest):
        os.system("echo {0}:{1} > {2}".format(access_key, secret_access_key, tmp_file))
        os.chmod(tmp_file, 0o600)
        os.system("s3fs {0} {1} -o passwd_file={2} -o use_path_request_style -o nonempty"
                  .format(bucket_name, folder_dest, tmp_file))

    def umount(self, folder_dest):
        os.system("umount {0}".format(folder_dest))
