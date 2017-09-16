#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen

from super_spider import app
"""
@author: peimingyuan
created on 2017/9/9 下午5:53
"""
config = app.config


def runserver(debug, port):
    debug = debug or config.get("DEBUG")
    if debug:
        app.run(
            host="0.0.0.0",
            port=port,
            debug=True
        )
    else:
        cmd = (
            "gunicorn "
            "-w gevent "
            "-b 0.0.0.0:{port} "
            "super_spider:app".format(port=port)
        )
        Popen(cmd, shell=True).wait()
