#!/usr/bin/python3
"""a Fabric script that distributes an archive
   to your web servers, using the function do_deploy
"""
from fabric.api import *
from fabric.operations import run, put
import os


env.hosts = ['100.25.211.130', '3.90.84.139']


def do_deploy(archive_path):
    """deploy codebase to our servers"""
    try:
        if not os.path.isfile(archive_path):
            return False
        put(archive_path, "/tmp/")
        tar_name = os.path.basename(archive_path)
        root, ext = os.path.splitext(tar_name)
        releases = "/data/web_static/releases"
        current = "/data/web_static/current"
        run("mkdir -p {}/{}".format(releases, root))
        run("tar xvf /temp/{} -C {}/{}".format(tar_name, releases, root))
        run("rm /tmp/{}".format(tar_name))
        run("rm -rf {}".format(current))
        run("mv {}/{}/web_static/* {}/{}"
            .format(releases, root, releases, root))
        run("rm -rf {}/{}/web_static".format(releases, root))
        run("ln -sf {}/{} {}".format(releases, root, current))
        return True
    except Exception:
        return False
