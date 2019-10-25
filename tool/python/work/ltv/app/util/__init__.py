# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:12
# @Author  : 馒头饺子
# @FileName: __init__.py.py
# @Software: PyCharm

from flask import Flask
from ..main import *

app = Flask(__name__)
app.register_blueprint(main)