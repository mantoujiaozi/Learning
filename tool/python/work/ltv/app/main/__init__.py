# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 15:51
# @Author  : 山风天下第一！！
# @FileName: __init__.py.py
# @Software: PyCharm



from flask import Blueprint

main = Blueprint('admin', __name__)

from . import api


