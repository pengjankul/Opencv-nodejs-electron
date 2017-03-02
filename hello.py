#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "test python web!!!"

if __name__ == "__main__":
    print('oh hello')
    #time.sleep(5)
    app.run(host='0.0.0.0', port=8000)

