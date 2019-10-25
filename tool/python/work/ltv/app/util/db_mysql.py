# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 12:01
# @Author  : 馒头饺子
# @FileName: db_mysql.py
# @Software: PyCharm

import pymysql
import pandas as pd


class MySQLdb:
    def __init__(self, dbconf):
        """
        初始化mysql
        :param dbconf:
        """
        self.db = pymysql.connect(host=dbconf['host'],
                                  port=dbconf['port'],
                                  user=dbconf['user'],
                                  passwd=dbconf['password'],
                                  db=dbconf['db'],
                                  charset=dbconf['charset'])
        self.cur = self.db.cursor()

    def select_sql_df(self, sql):
        """
        查询sql，返回一个Dataframe
        :param sql:
        :return:
        """
        df = pd.read_sql(sql, con=self.db)
        return df

    def select_sql(self, sql):
        """
        查询sql，返回一个二维元组
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.db.commit()
        return result

    def change_sql(self, sql):
        """
        更新,或者插入
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.db.commit()

    def close(self):
        """
        关闭
        :return:
        """
        self.db.close()
        self.cur.close()
