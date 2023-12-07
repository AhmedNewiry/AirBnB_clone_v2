#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
   from the contents of the web_static
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the
       contents of the web_static
    """
    date_time = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions")
    f_path = "versions/web_static_{}.tgz".format(date_time)
    tar = local('tar -cfvz {} web_static'.format(f_path))
    if tar.failed:
        return None
    return path
