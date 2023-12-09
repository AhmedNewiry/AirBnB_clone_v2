#!/usr/bin/python3
"""A module contianing th do_delete function"""
from fabric.api import *
from fabric.context_managers import lcd, cd
import os
from datetime import datetime
from pathlib import Path

env.user = "ubuntu"
env.hosts = ['100.25.194.46', '100.25.194.197']


def do_clean(number=0):
    """a method that delete the unrequired tar files"""
    tar_files = []
    r_tar_files = []
    number = int(number)
    if number <= 2:

        tar_files = sorted(os.listdir('./versions'),
                           key=lambda x: datetime.strptime(os.path.splitext(x)[0][12:],
                                                           '%Y%m%d%H%M%S'),
                           reverse=True)
        print(tar_files[0])
        if number == 2:
            with lcd('./versions'):
                local(
                    "sudo ls | grep -v -e {} -e {} | xargs rm -f".format(
                        tar_files[0], tar_files[1]))
            with cd('/data/web_static/releases'):
                sudo("ls | grep -v -e {} -e {} | xargs rm -rf".format(
                    os.path.splitext(tar_files[0])[0], os.path.splitext(tar_files[1])[0]))
        elif number == 1 or number == 0:
            with lcd('./versions'):
                local(
                    "sudo ls | grep -v {} | xargs rm -f".format(tar_files[0]))
            with cd('/data/web_static/releases'):
                sudo("ls | grep -v {} | xargs rm -rf".format(os.path.splitext(tar_files[0])[0]))                                                                          
