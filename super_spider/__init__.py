#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
"""
@author: peimingyuan
created on 2017/9/9 下午5:51
"""

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
