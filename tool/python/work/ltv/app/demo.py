# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:48
# @Author  : 山风天下第一！！
# @FileName: demo.py
# @Software: PyCharm

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test',
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin',
        'done': False
    }
]

# 这行代码的'/',对应下面的函数定义def home(),调试的网址“http://127.0.0.1:5000/”
# 如果是'/ospaf',对应的函数定义def ospaf()，调试的网址“http://127.0.0.1:5000/ospaf”
@app.route('/', methods=['POST'])
def home():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)