# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 11:51
# @Author  : 馒头饺子
# @FileName: db_impala.py
# @Software: PyCharm

from impala.dbapi import connect
from impala.util import as_pandas


class ImpalaDb:
    def __init__(self, dbconf):
        """
        初始化impala
        :param dbconf:
        """
        self.db = connect(host=dbconf['host'], port=dbconf['port'])
        self.cur = self.db.cursor()

    def select_sql_df(self, sql):
        """
        查找，返回一个Dataframe
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        df = as_pandas(self.cur)
        return df

    def insert_sql(self, sql):
        """
        插入
        :return:
        """
        self.cur.execute(sql)


    def close(self):
        """
        关闭当前连接
        :return:
        """
        self.db.close()



