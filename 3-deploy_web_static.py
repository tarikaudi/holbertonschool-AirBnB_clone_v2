#!/usr/bin/python3
# comment for the checker

from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['54.158.0.253', '3.95.238.142']


def do_deploy(archive_path):
    """deploy function"""

    tok = archive_path.split('/')
    fileN = tok[-1].split('.')[0]
    uncompressed = "/data/web_static/releases/" + fileN + "/"

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p " + uncompressed)
        run("tar -xzf /tmp/" + fileN + ".tgz -C " + uncompressed)
        run("rm /tmp/" + fileN + ".tgz")
        run("mv " + uncompressed + "web_static/* " + uncompressed)
        run("rm -rf " + uncompressed + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + uncompressed + " /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False

def do_pack():
    """func pack"""
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

def deploy():
    """deploy func"""
    archive_path = do_pack()
    if not archive_path:
        return False
    d_d = do_deploy(archive_path)
    return d_d
