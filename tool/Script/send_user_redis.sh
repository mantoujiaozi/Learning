#!/bin/sh
#发送作弊用户的id到redis。只需要传入impala 中的表名（包括库名）和标识作弊用户的id字段，命中规则字段。 
#

cd `dirname $0`
impala_table_name=$1
user_column_name=$2
reason_column_name=$3

#select  invite_user from tmp.tmp limit 1 "

rm -rf ../data/user_reuslt.txt
rm -rf ../data/user_expire.txt
#redis-cli -n 0 -h 172.16.11.171 -a coohua flushdb
sleep 3
# 如果规则列没有传入，默认写入的redis key的值为字符串null
if [ -z $reason_column_name ];then
   impala-shell -B -q "select ' set',$user_column_name ,'null'  from $impala_table_name" -o ../data/user_result.txt
else
   impala-shell -B -q "select ' set',$user_column_name , $reason_column_name  from $impala_table_name" -o ../data/user_result.txt
fi
cat ../data/user_result.txt |gawk '{print "expire " $2 " 86400"}' > ../data/user_expire.txt
unix2dos ../data/user_result.txt 
unix2dos ../data/user_expire.txt
cat ../data/user_result.txt|redis-cli -n 0 -h 172.16.11.171 -a coohua --pipe
cat ../data/user_expire.txt|redis-cli -n 0 -h 172.16.11.171 -a coohua --pipe
