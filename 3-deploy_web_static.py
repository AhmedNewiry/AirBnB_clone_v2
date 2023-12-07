#!/usr/bin/python3
"""a Fabric script that creates and distributes
   an archiveto your web servers, using the function deploy
"""


from fabric.api import *
from datetime import datetime
import os


env.hosts = ["100.25.194.46", "100.25.194.197"]
env.user = "ubuntu"


def do_pack():
    """generates a .tgz archive from the
       contents of the web_static
    """
    date_time = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions")
    f_path = "versions/web_static_{}.tgz".format(date_time)
    tar = local('tar cfvz {} web_static'.format(f_path))
    if tar.failed:
        return None
    return path


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
        run("tar xvf /tmp/{} -C {}/{}".format(tar_name, releases, root))
        run("rm /tmp/{}".format(tar_name))
        run("rm -rf {}".format(current))
        run("mv {}/{}/web_static/* {}/{}"
            .format(releases, root, releases, root))
        run("ln -sf {}/{} {}".format(releases, root, current))
        return True
    except Exception:
        return False


def deploy():
    """calls both functions pack and deploy"""
    tar_path = do_pack()
    if tar_path is None:
        return False
    return do_deploy(tar_path)
