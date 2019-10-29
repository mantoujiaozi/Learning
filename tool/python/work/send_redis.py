# -*- coding: utf-8 -*-

from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd
import redis
import time
import datetime
import json

yestoday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d")
current_milli_time = lambda: int(round(time.time() * 1000))


conn = connect(host='idc-002-gateway', port=21050)
cur = conn.cursor()
rds = redis.Redis(host='dp.coohua.com', port=6379, db=1, password="coohua", decode_responses=True)

def taonewslabel():
    pipe = rds.pipeline()
    #key_list = rds.keys('*')
    #for key in key_list:
    #    if "taonewslabel_" in key:
    #        pipe.delete(key)
    #pipe.execute()
    #pipe = rds.pipeline()
    #print "taonewslabel  delete"
    cur.execute("select userid,GROUP_CONCAT(cast(type as string)) as tags  from reports.taonew_label_user where logday='%s' group by userid;" % yestoday)
    df = as_pandas(cur)
    dict1 = dict()
    dict1['error_code'] = 0
    for index, row in df.iterrows():
        dict1['userid'] = row['userid']
        list = row['tags'].split(',')
        list = map(int, list)
        dict1['tags'] = list
        json_str = json.dumps(dict1)
        pipe.set('taonewslabel_' + row['userid'],json_str)
	if index%1000 == 0:
            pipe.execute()
    pipe.execute()
    print "taonewslabel finished."



taonewslabel()
cur.close()
conn.close()
