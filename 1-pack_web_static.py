#!/usr/bin/python3
# comment for the checker upto

from fabric.api import local
from datetime import datetime


def do_pack():
    """comment for the func"""
    try:
        local("mkdir -p versions")
        date = datetime.now()
        time = date.strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + time + ".tgz"
        time = "tar -cvzf " + name + " web_static"
        local(time)
        return name
    except:
        return None

