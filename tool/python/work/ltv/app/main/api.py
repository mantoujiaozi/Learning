# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:16
# @Author  : 馒头饺子
# @FileName: api.py
# @Software: PyCharm


from flask import jsonify
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    tasks = (
        {
            'id': 1,
            'title': '搞事',
            'description': u'This is ospaf-api test',
            'done': False
        },
        {
            'id': 2,
            'title': '要死',
            'description': u'I am garvin',
            'done': False
        }
    )
    return jsonify({'tasks': tasks})
