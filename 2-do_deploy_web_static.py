#!/usr/bin/python3
"""a Fabric script that distributes an archive
   to your web servers, using the function do_deploy
"""
from fabric.api import *
from fabric.operations import run, put
import os


env.hosts = ['100.25.194.46', '100.25.194.197']


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
        run("sudo mkdir -p {}/{}".format(releases, root))
        run("sudo tar xvf /tmp/{} -C {}/{}".format(tar_name, releases, root))
        run("sudo rm /tmp/{}".format(tar_name))
        run("sudo rm -rf {}".format(current))
        run("sudo mv {}/{}/web_static/* {}/{}"
            .format(releases, root, releases, root))
        run("sudo rm -rf {}/{}/web_static".format(releases, root))
        run("sudo ln -sf {}/{} {}".format(releases, root, current))
        return True
    except Exception:
        return False
